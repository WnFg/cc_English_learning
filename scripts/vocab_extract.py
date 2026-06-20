#!/usr/bin/env python3
"""Extract one vocab unit's text from the PDF — the progressive engine.

Only ever reads a few pages, so the 1,633-page book never loads at once.

Usage:
    python3 scripts/vocab_extract.py --unit 182      # look up page range in the index
    python3 scripts/vocab_extract.py --pages 673-676 # explicit 1-indexed page range

Prints cleaned UTF-8 text (Step1 场景词 + Step2 学以致用). The /vocab skill reads this
and selects/formats the 8–12 words to teach — keeping parsing robust to the book's
line-broken layout.
"""
import argparse
import os
import re
import sys

from pypdf import PdfReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "materials", "vocab-book.pdf")
INDEX = os.path.join(ROOT, "curriculum", "vocab-index.md")


def unit_page_range(unit_no):
    """Return (start, end) 1-indexed pages for a unit from the index, or None."""
    if not os.path.exists(INDEX):
        sys.exit(f"Index not found at {INDEX} — run scripts/vocab_build_index.py first.")
    with open(INDEX, encoding="utf-8") as f:
        for line in f:
            cells = [c.strip() for c in line.strip().split("|")]
            # rows look like: ['', '182', 'title', 'chapter', '673', '676', '']
            if len(cells) >= 6 and cells[1].isdigit() and int(cells[1]) == unit_no:
                return int(cells[4]), int(cells[5])
    return None


def clean(text):
    """Collapse the runs of blank lines the PDF layout produces."""
    out = []
    blanks = 0
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.strip():
            out.append(line)
            blanks = 0
        else:
            blanks += 1
            if blanks == 1:
                out.append("")
    return "\n".join(out).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--unit", type=int, help="unit number from curriculum/vocab-index.md")
    g.add_argument("--pages", help="explicit 1-indexed page range, e.g. 673-676")
    args = ap.parse_args()

    if not os.path.exists(PDF):
        sys.exit(f"PDF not found at {PDF} — copy the vocab book there first.")

    if args.unit is not None:
        rng = unit_page_range(args.unit)
        if rng is None:
            sys.exit(f"Unit {args.unit} not found in {INDEX}.")
        start, end = rng
    else:
        m = re.match(r"^(\d+)-(\d+)$", args.pages.strip())
        if not m:
            sys.exit("--pages must look like 673-676")
        start, end = int(m.group(1)), int(m.group(2))

    reader = PdfReader(PDF)
    n = len(reader.pages)
    start = max(1, start)
    end = min(n, end)

    print(f"# Unit pages {start}-{end} of {n}\n")
    for p in range(start, end + 1):
        text = clean(reader.pages[p - 1].extract_text() or "")
        if text:
            print(f"----- page {p} -----")
            print(text)
            print()


if __name__ == "__main__":
    main()
