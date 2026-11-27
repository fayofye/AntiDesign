#!/usr/bin/env python3
"""Write a skeleton copy of a page: fonts, colours, shadows and images stripped, every box outlined.

Screenshot the skeleton of a design beside the skeleton of the baseline. If the shapes match
(where the hero sits, how the navigation reads, how many pricing columns), the traits that live
in the shape are kept, whatever the skin says.

    python3 scripts/skeleton.py path/to/page.html   ->  path/to/page.skeleton.html

The copy sits beside the page so its relative links still work. Delete it when you are done.
Standard library only.
"""
import sys
from pathlib import Path

MARK = "antidesign-skeleton"
# shortcut: a page rule marked !important with a class or id still beats these; raise specificity if colour survives.
CSS = f"""<style id="{MARK}">
*,*::before,*::after{{font-family:system-ui,sans-serif!important;font-style:normal!important;font-weight:400!important;
letter-spacing:normal!important;text-transform:none!important;text-shadow:none!important;color:#000!important;
background:transparent!important;border-color:#999!important;box-shadow:none!important;filter:none!important;
backdrop-filter:none!important;border-radius:0!important;outline:1px solid #0003!important;
animation:none!important;transition:none!important}}
html,body{{background:#fff!important}}
img,video,canvas,svg,iframe,picture{{opacity:.25!important;background:#888!important}}
</style>
"""


def skeleton(page: str) -> str:
    """Return the page with the skeleton stylesheet last, so it wins over the page's own rules."""
    at = page.lower().rfind("</body>")
    out = page[:at] + CSS + page[at:] if at >= 0 else page + CSS
    assert out.count(MARK) == page.count(MARK) + 1, "skeleton stylesheet not inserted"
    return out


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith((".html", ".htm")):
        sys.exit("usage: python3 scripts/skeleton.py path/to/page.html")
    src = Path(sys.argv[1])
    dst = src.with_name(src.stem + ".skeleton.html")
    dst.write_text(skeleton(src.read_text(encoding="utf-8")), encoding="utf-8")
    print(dst)


if __name__ == "__main__":
    main()
