#!/usr/bin/env python3
"""Turn a PDF (URL or local file) into Markdown inside a question's ``raw/`` folder.

Resolution sources are often PDFs (USDA export sales, state health bulletins,
central-bank reports). ``WebFetch`` cannot always read them and ``pdftotext`` is not
on the CI allow list, so the forecaster runs this instead -- it is reachable through
the ``uv run python`` permission the session already holds.

The PDF itself is kept in the system temp directory, never in the repository: the
repo carries no binary files (the MCP push fallback cannot send them, and the
guard would delete anything written outside the question folder anyway). Only the
extracted Markdown lands in ``questions/<slug>/raw/<stem>-<YYYY-MM-DD>.md``, with
the source URL and page range in its first line, so the evidence trail stays
text and dated like every other ``raw/`` file.

Tables come out as Markdown tables (pymupdf4llm), which is the point of using it
over plain text extraction: the numbers a forecast rests on usually sit in one.

Examples
--------
    uv run python scripts/pdf_text.py https://apps.fas.usda.gov/esrqs/StaticReports/WeeklyHighlightsReport.pdf \\
        2026-10-19-mc46141-u-s-wheat-net-export-sales-usda
    uv run python scripts/pdf_text.py <url> <slug> --pages 1-3,12 --name fdoh-arbovirus-w40
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import QUESTIONS, find_slug, today

# Plain bot agent with a contact URL, deliberately not "Mozilla/...": bot shields
# (USDA's, checked 2026-10-19) reset the connection when a browser agent arrives
# over Python's TLS fingerprint, but let an honest bot agent through.
USER_AGENT = "claude-forecasting-bot/1.0 (+https://github.com/m-ad/claude_forecasting_auto)"
MAX_BYTES = 50 * 1024 * 1024
# Layout analysis costs ~0.1-0.5 s a page; 30 pages keeps a default run well under a
# minute and covers every weekly bulletin seen so far. Longer reports: pass --pages.
DEFAULT_MAX_PAGES = 30
PREVIEW_CHARS = 6000


def parse_pages(spec: str, n_pages: int) -> list[int]:
    """1-based ``"1-5,9"`` into sorted 0-based page indices that exist.

    Raises
    ------
    ValueError
        On a malformed spec or one that selects no existing page.
    """
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        m = re.fullmatch(r"(\d+)(?:-(\d+))?", part)
        if not m:
            raise ValueError(f"bad page range {part!r}; use e.g. 1-5,9")
        lo = int(m.group(1))
        hi = int(m.group(2) or lo)
        if lo < 1 or hi < lo:
            raise ValueError(f"bad page range {part!r}")
        pages.update(range(lo - 1, min(hi, n_pages)))
    if not pages:
        raise ValueError(f"--pages {spec!r} selects nothing in a {n_pages}-page PDF")
    return sorted(pages)


def stem_for(source: str, name: str | None) -> str:
    """A file-name stem: ``--name`` if given, else the PDF's own name, slugified."""
    base = name or Path(source.split("?")[0].rstrip("/")).stem or "document"
    stem = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:60]
    return stem or "document"


def fetch(url: str) -> Path:
    """Download ``url`` to the temp directory and return the path.

    Raises
    ------
    RuntimeError
        On an HTTP or network error, an oversized body, or a body that is not a PDF
        (an HTML landing page is the common case: the message says to use WebFetch).
    """
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read(MAX_BYTES + 1)
            ctype = resp.headers.get("Content-Type", "?")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from None
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise RuntimeError(f"could not fetch {url}: {exc}") from None
    if len(body) > MAX_BYTES:
        raise RuntimeError(f"{url} is larger than {MAX_BYTES // 2**20} MB")
    if not body.lstrip()[:5].startswith(b"%PDF"):
        raise RuntimeError(
            f"{url} did not return a PDF (Content-Type {ctype}); "
            "if it is a web page, read it with WebFetch instead"
        )
    folder = Path(tempfile.gettempdir()) / "pdf_text"
    folder.mkdir(exist_ok=True)
    path = folder / f"{hashlib.sha256(url.encode()).hexdigest()[:16]}.pdf"
    path.write_bytes(body)
    return path


def convert(pdf: Path, pages_spec: str | None) -> tuple[str, list[int], int]:
    """``(markdown, 0-based pages converted, total pages)`` for ``pdf``."""
    # Imported here so --help and the tests of the pure helpers stay fast.
    import pymupdf
    import pymupdf4llm

    with pymupdf.open(pdf) as doc:
        n_pages = doc.page_count
    if pages_spec:
        pages = parse_pages(pages_spec, n_pages)
    else:
        pages = list(range(min(n_pages, DEFAULT_MAX_PAGES)))
    md = pymupdf4llm.to_markdown(str(pdf), pages=pages, show_progress=False)
    return md, pages, n_pages


def page_label(pages: list[int]) -> str:
    """0-based indices back into a compact 1-based ``"1-5,9"``."""
    runs: list[list[int]] = []
    for p in pages:
        if runs and p == runs[-1][1] + 1:
            runs[-1][1] = p
        else:
            runs.append([p, p])
    return ",".join(f"{a + 1}" if a == b else f"{a + 1}-{b + 1}" for a, b in runs)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("source", help="PDF URL (http/https) or a local path")
    ap.add_argument("slug", help="question folder the Markdown is written into")
    ap.add_argument(
        "--pages",
        help=f"1-based pages, e.g. 1-5,9 (default: the first {DEFAULT_MAX_PAGES})",
    )
    ap.add_argument("--name", help="file-name stem (default: the PDF's own name)")
    args = ap.parse_args()

    slug = find_slug(args.slug) or sys.exit(f"! no unique question for {args.slug!r}")
    try:
        if re.match(r"https?://", args.source):
            pdf = fetch(args.source)
        else:
            pdf = Path(args.source)
            if not pdf.is_file():
                sys.exit(f"! no such file: {pdf}")
        md, pages, n_pages = convert(pdf, args.pages)
    except (RuntimeError, ValueError) as exc:
        sys.exit(f"! {exc}")
    except Exception as exc:  # noqa: BLE001 -- a corrupt PDF must not cost a debug loop
        sys.exit(f"! could not read the PDF: {type(exc).__name__}: {exc}")

    out = QUESTIONS / slug / "raw" / f"{stem_for(args.source, args.name)}-{today()}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    retrieved = dt.datetime.now(dt.UTC).isoformat(timespec="seconds")
    header = (
        f"<!-- source: {args.source} | retrieved: {retrieved} | "
        f"pages {page_label(pages)} of {n_pages} -->\n\n"
    )
    out.write_text(header + md, encoding="utf-8")

    print(f"wrote {out.relative_to(QUESTIONS.parent)}: pages {page_label(pages)} "
          f"of {n_pages}, {len(md):,} characters")
    if len(pages) < n_pages:
        print(f"note: {n_pages - len(pages)} page(s) not converted; pass --pages for them")
    if not md.strip():
        print("note: no text layer (a scanned PDF?); nothing to extract")
        return
    print(f"--- first {min(len(md), PREVIEW_CHARS):,} characters "
          "(Read or Grep the file for the rest) ---")
    print(md[:PREVIEW_CHARS])


if __name__ == "__main__":
    main()
