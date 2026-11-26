#!/usr/bin/env python3
"""Roll designs from a table of unusual choices: 6 traits x 10 options = 1,000,000 designs.

Each roll draws six random 6-digit numbers and picks one of them; each digit of the
picked number selects one option per trait. Build what it rolls; do not reroll for taste.
"""
import argparse
import secrets

TRAITS = [
    ("Structure", ["Horizontal-only scroll", "One screen, no scroll; content swaps in place",
                   "A 2D surface you drag around", "The whole page is one spreadsheet",
                   "The page is a chat transcript", "A stack of cards you flip",
                   "Split screen, the halves scroll in opposite directions", "Radial: content set on circles",
                   "Vertical columns read top to bottom, right to left", "A terminal session"]),
    ("Type", ["Pixel font (Silkscreen)", "Blackletter (UnifrakturCook)", "Marker handwriting (Permanent Marker)",
              "Worn typewriter (Special Elite)", "Stencil (Big Shoulders Stencil)",
              "Ultra-condensed giant caps (Six Caps)", "Inline neon tubes (Monoton)", "Comic Neue against Times",
              "Copperplate script (Pinyon Script)", "A colour 3D font (Nabla)"]),
    ("Colour", ["Hi-vis orange and navy", "Pure RGB primaries", "Pastel candy", "Thermal camera",
                "Sepia photograph", "Hazard yellow and black", "Blueprint cyan on prussian",
                "Vaporwave pink and cyan", "Riso fluorescent pink and teal", "Mid-grey only"]),
    ("Hero", ["A working game", "A form you fill before you see anything", "A receipt that prints",
              "A countdown to the next important date", "A card or coin you can turn over",
              "A spotlight under the cursor; the rest is dark", "A quiz", "A slot machine",
              "One giant number counting", "A map"]),
    ("Texture", ["Halftone dots", "CRT scanlines and glow", "Paper grain and torn edges", "Glitch and RGB split",
                 "Wobbly hand-drawn borders", "Dithered gradients", "Stickers and tape",
                 "Marquee tickers everywhere", "Hard offset shadows", "None: raw, unstyled HTML"]),
    ("Voice", ["A legal contract", "A recipe", "A weather forecast", "Sports commentary", "Classified ads",
               "Museum wall labels", "An assembly manual", "A horoscope", "A field guide", "A boarding pass"]),
]
assert len(TRAITS) == 6 and all(len(options) == 10 for _, options in TRAITS)  # exactly 10**6 designs


def roll():
    """Return the six drawn numbers, the picked one, and its (trait, option) pairs."""
    drawn = [f"{secrets.randbelow(1_000_000):06d}" for _ in range(6)]
    picked = secrets.choice(drawn)
    return drawn, picked, [(name, options[int(d)]) for (name, options), d in zip(TRAITS, picked)]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--count", type=int, default=1, help="how many designs to roll (default 1)")
    args = parser.parse_args()
    if args.count < 1:
        parser.error("--count must be 1 or more")
    for _ in range(args.count):
        drawn, picked, spec = roll()
        print(f"Design {picked}  (drawn: {' '.join(drawn)})")
        for name, option in spec:
            print(f"  {name}: {option}")


if __name__ == "__main__":
    main()
