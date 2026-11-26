#!/usr/bin/env python3
"""Roll designs from a table of unusual choices: 10 traits x 10 options = 10,000,000,000 designs.

The traits match the skill's default table, so every trait of a rolled design is decided.
Each roll draws six random 10-digit numbers and picks one; each digit selects one option per trait.
Build what it rolls; do not reroll for taste.
"""
import argparse
import secrets

TRAITS = [
    ("Reading direction", ["Horizontal-only scroll", "One screen, no scroll; content swaps in place",
                           "Vertical columns read top to bottom, right to left", "Bottom to top",
                           "Zoom in to read: each level is closer", "A 2D surface you drag around",
                           "Split screen, the halves scroll in opposite directions", "Read around a circle",
                           "Diagonal: content laid on a slope", "Page turns, like a book"]),
    ("Layout", ["Blocks sized by the product's own numbers", "One real-world object fills the page",
                "Overlapping layers, nothing aligned", "One giant spreadsheet", "A chat transcript",
                "A terminal session", "A map with pins", "A timeline running off both edges",
                "A stack of cards you flip", "Everything inside one drawing"]),
    ("Hero", ["A working game", "A form you fill before you see anything", "A receipt that prints",
              "A countdown to the next important date", "A card or coin you can turn over",
              "A spotlight under the cursor; the rest is dark", "A quiz", "A slot machine",
              "One giant number counting", "A 3D liquid surface (elements/liquid-3d.html)"]),
    ("Components", ["Ledger rows", "Coupons with perforations", "Tickets with stubs", "Specimen cards",
                    "Index tabs down one edge", "Rubber stamps", "A scoreboard", "Sticky notes",
                    "Receipts", "Margin notes in pencil"]),
    ("Type", ["Pixel font (Silkscreen)", "Blackletter (UnifrakturCook)", "Marker handwriting (Permanent Marker)",
              "Worn typewriter (Special Elite)", "Stencil (Big Shoulders Stencil)",
              "Ultra-condensed giant caps (Six Caps)", "Inline neon tubes (Monoton)", "Comic Neue against Times",
              "Copperplate script (Pinyon Script)", "A colour 3D font (Nabla)"]),
    ("Colour", ["Hi-vis orange and navy", "Pure RGB primaries", "Pastel candy", "Thermal camera",
                "Sepia photograph", "Hazard yellow and black", "Blueprint cyan on prussian",
                "Vaporwave pink and cyan", "Riso fluorescent pink and teal", "Mid-grey only"]),
    ("Texture", ["Halftone dots", "CRT scanlines and glow", "Paper grain and torn edges", "Glitch and RGB split",
                 "Wobbly hand-drawn borders", "Dithered gradients", "Stickers and tape",
                 "Marquee tickers everywhere", "Hard offset shadows", "Guilloché and microtext"]),
    ("Pricing", ["Blocks sized by price", "One sentence", "Coupons to detach", "Seat classes",
                 "A fee schedule table", "A menu with prices", "A price tag on a string",
                 "A slot machine that lands on a plan", "Team sheets", "A receipt total"]),
    ("Voice", ["A legal contract", "A recipe", "A weather forecast", "Sports commentary", "Classified ads",
               "Museum wall labels", "An assembly manual", "A horoscope", "A field guide", "A boarding pass"]),
    ("Motion", ["A WebGL shader", "A number counting", "Spinning reels", "Glitch", "Typing, like a terminal",
                "Parallax that tilts in 3D", "Things that follow the cursor", "A marker moving along a line",
                "Pages that flip", "Shapes that morph into each other"]),
]
assert len(TRAITS) == 10 and all(len(options) == 10 for _, options in TRAITS)  # exactly 10**10 designs


def roll():
    """Return the six drawn numbers, the picked one, and its (trait, option) pairs."""
    drawn = [f"{secrets.randbelow(10 ** len(TRAITS)):0{len(TRAITS)}d}" for _ in range(6)]
    picked = secrets.choice(drawn)
    return drawn, picked, [(name, options[int(d)]) for (name, options), d in zip(TRAITS, picked)]


def main():
    names = [name for name, _ in TRAITS]
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--count", type=int, default=1, help="how many designs to roll (default 1)")
    parser.add_argument("--trait", help="roll one option for a single trait: " + ", ".join(names))
    args = parser.parse_args()
    if args.trait:
        match = [t for t in TRAITS if t[0].lower().startswith(args.trait.lower())]
        if not match:
            parser.error(f"unknown trait {args.trait!r}; pick one of: " + ", ".join(names))
        name, options = match[0]
        print(f"{name}: {secrets.choice(options)}")
        return
    if args.count < 1:
        parser.error("--count must be 1 or more")
    for _ in range(args.count):
        drawn, picked, spec = roll()
        print(f"Design {picked}  (drawn: {' '.join(drawn)})")
        for name, option in spec:
            print(f"  {name}: {option}")


if __name__ == "__main__":
    main()
