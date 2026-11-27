#!/usr/bin/env python3
"""Roll designs from tables of unusual choices: 11 traits x 10 options = 100,000,000,000 designs per tone.

The traits match the skill's default table, so every trait of a rolled design is decided.
Two tones: loud (strange on purpose) and quiet (unusual, but credible for a bank or a law firm).
Each roll draws six random 11-digit numbers and picks one; each digit selects one option per trait.
Build what it rolls; do not reroll for taste.
--keep locks traits the brand already owns. --movement rolls a design movement to follow instead.
--library rolls specimens from one page of library/.
"""
import argparse
import html
import re
import secrets
from pathlib import Path

LIBRARY = Path(__file__).resolve().parent.parent / "library"
SPEC = re.compile(r'<article class="spec" id="([a-z]+-\d\d)" data-name="([^"]+)">')
POINTER = re.compile(r"\((library/[a-z]+\.html)#([a-z]+-\d\d)\)")
TONES = ("loud", "quiet")
LOCKED = "Locked: build it from the brand"

TRAITS = [
    ("Reading direction", {
        "loud": ["Horizontal-only scroll (library/layouts.html#lay-01)",
                 "One screen, no scroll; content swaps in place (library/layouts.html#lay-02)",
                 "Vertical columns read top to bottom, right to left (library/layouts.html#lay-03)",
                 "Bottom to top (library/layouts.html#lay-04)",
                 "Zoom in to read: each level is closer (library/layouts.html#lay-05)",
                 "A 2D surface you drag around (library/layouts.html#lay-06)",
                 "Split screen, the halves scroll in opposite directions (library/layouts.html#lay-07)",
                 "Read around a circle (library/layouts.html#lay-08)",
                 "Diagonal: content laid on a slope (library/layouts.html#lay-09)",
                 "Page turns, like a book (library/layouts.html#lay-10)"],
        "quiet": ["Newspaper columns: down one, then the next", "An index first; each entry opens its section in place",
                  "Half the content in the margin as sidenotes", "One sentence per screen, read in order",
                  "Contents with numbered pages, like a book", "Questions down the left, answers down the right",
                  "Zoom out to read: it opens close on one detail", "Facing pages: the screen is a spread",
                  "A ruled timeline down the left edge; everything hangs off a date",
                  "Nested clauses numbered 1, 1.1, 1.1.1, like a contract"]}),
    ("Layout", {
        "loud": ["Blocks sized by the product's own numbers", "One real-world object fills the page",
                 "Overlapping layers, nothing aligned", "One giant spreadsheet", "A chat transcript",
                 "A terminal session", "A map with pins", "A timeline running off both edges",
                 "A stack of cards you flip", "Everything inside one drawing"],
        "quiet": ["An asymmetric grid, everything flush left of centre, one block breaking it", "An editorial grid: captions, pull quotes, a folio",
                  "A datasheet: specification tables and line drawings", "A book page: wide margins and a running head",
                  "A specimen sheet: the product at many sizes on one plane",
                  "A catalogue: numbered entries with plates and captions",
                  "An architect's sheet: a title block, gridlines lettered A to F and numbered 1 to 8",
                  "A letter: one column, a date, a salutation, a signature",
                  "A timetable grid: rows of times, columns of places", "A form: numbered boxes, all the content inside them"]}),
    ("Navigation", {
        "loud": ["A table of contents that is the hero", "A command line: type where to go, with the links listed under it",
                 "A dial you turn to pick a section", "A map legend: each section is a place",
                 "Channel numbers you flip through", "Footnotes: every link is a numbered note",
                 "A departure board listing every section", "A floor plan: each room is a section",
                 "A tracklist with running times", "One sentence where each phrase is a link"],
        "quiet": ["Running heads: the section name top left, a page number top right",
                  "A fixed index in the margin, set small", "Each section ends with the contents, its own entry marked",
                  "Footer only; the top stays empty", "Next and previous only, like turning pages",
                  "A colophon that lists every section", "An A to Z index at the foot of the page",
                  "A ruler down the left edge, sections as its marks", "Breadcrumbs as the only navigation",
                  "Section numbers set large in the margin, each one a link"]}),
    ("Hero", {
        "loud": ["A working game", "A form you fill before you see anything", "A receipt that prints",
                 "A countdown to the next important date", "A card or coin you can turn over",
                 "A spotlight under the cursor; the rest is dark", "A quiz", "A slot machine",
                 "One giant number counting", "A 3D liquid surface (elements/liquid-3d.html)"],
        "quiet": ["The one key figure, set huge and still, its working shown small", "One sentence set very large, nothing else",
                  "A plain table that answers the first question", "The first page of the document the product makes",
                  "Before and after in two plain columns of text", "A dimensioned line drawing of the product",
                  "A status line with the product's real current state",
                  "A quotation from the product's own docs, set as an epigraph",
                  "A calculation set out like a sum on paper", "A photograph cropped hard to one detail, with a caption"]}),
    ("Components", {
        "loud": ["Ledger rows", "Coupons with perforations", "Tickets with stubs", "Specimens pinned on one big board",
                 "Index tabs down one edge", "Rubber stamps", "A scoreboard", "Notes clipped to a line, at angles",
                 "Receipts", "Margin notes in pencil"],
        "quiet": ["Rows ruled by hairlines, numbers hanging in the margin", "Sidenotes and footnotes",
                  "Numbered figures with captions", "Definition lists: term left, meaning right", "Pull quotes between rules",
                  "Specification tables", "Small-caps labels over plain paragraphs, no boxes at all",
                  "Reference numbers and dates set at each block's corner", "Annotations: thin leader lines out to labels",
                  "Drop caps opening each section"]}),
    ("Type", {
        "loud": ["Pixel font (Silkscreen)", "Blackletter (UnifrakturCook)", "Marker handwriting (Permanent Marker)",
                 "Worn typewriter (Special Elite)", "Stencil (Big Shoulders Stencil)",
                 "Ultra-condensed giant caps (Six Caps)", "Inline neon tubes (Monoton)", "Comic Neue against Times",
                 "Copperplate script (Pinyon Script)", "A colour 3D font (Nabla)"],
        "quiet": ["One grotesk at only two sizes, giant and small (Archivo)", "Monospace only (Spline Sans Mono)",
                  "A text serif with optical sizes for everything (Literata)",
                  "Wide caps over a book serif (Archivo at width 125, Crimson Pro)", "A slab serif throughout (Bitter)",
                  "Small caps and old-style figures throughout (Spectral, Spectral SC)",
                  "Condensed grotesk caps, tightly set (Barlow Condensed)",
                  "Old grotesque heads over plain text (Darker Grotesque)",
                  "Didone hairlines, at large sizes only (Bodoni Moda)",
                  "A serif and a mono, no sans (Source Serif 4, Source Code Pro)"]}),
    ("Colour", {
        "loud": ["Hi-vis orange and navy", "Pure RGB primaries", "Pastel candy", "Thermal camera",
                 "Sepia photograph", "Hazard yellow and black", "Blueprint cyan on prussian",
                 "Vaporwave pink and cyan", "Riso fluorescent pink and teal", "Mid-grey only"],
        "quiet": ["Black on newsprint grey with one spot red", "Two inks off-register by a hair: blue and red on white",
                  "Black and white; one photograph carries all the colour", "Fountain-pen blue on white",
                  "Olive, ochre and slate, like a survey map", "Ledger green and gold", "Warm grey with one safety orange",
                  "Burgundy on cool stone grey", "Black on pale blue graph paper",
                  "The browser's own: black, link blue, visited purple"]}),
    ("Texture", {
        "loud": ["Halftone dots (library/textures.html#tex-01)", "CRT scanlines and glow (library/textures.html#tex-02)",
                 "Paper grain and torn edges (library/textures.html#tex-03)",
                 "Glitch and RGB split (library/textures.html#tex-04)",
                 "Wobbly hand-drawn borders (library/textures.html#tex-05)",
                 "Dithered gradients (library/textures.html#tex-06)", "Stickers and tape",
                 "Marquee tickers everywhere", "Hard offset shadows",
                 "Guilloché and microtext (elements/security-print.html)"],
        "quiet": ["Hairline rules, nothing else", "Paper grain only (library/textures.html#tex-03)",
                  "Engraved hatching (library/textures.html#tex-07)",
                  "Crop and registration marks (library/textures.html#tex-08)",
                  "A visible baseline grid (library/textures.html#tex-09)", "Blind emboss (library/textures.html#tex-10)",
                  "Duotone photographs (library/textures.html#tex-11)", "A faint dot grid",
                  "Pencil construction lines left in", "Letterpress bite (library/motion.html#mo-03)"]}),
    ("Pricing", {
        "loud": ["Blocks sized by price", "One sentence", "Coupons to detach", "Seat classes",
                 "A fee schedule table", "A menu with prices", "A price tag on a string",
                 "A slot machine that lands on a plan", "Team sheets", "A receipt total"],
        "quiet": ["A rate card: one column, prices aligned on the decimal", "A paragraph of prose with the numbers in it",
                  "A calculator: enter your use, see your price", "Dotted leaders to each price, like a contents page",
                  "An itemised estimate with a total", "Prices in the margin beside the features they buy",
                  "A schedule of charges in numbered clauses", "The unit price first, then worked examples",
                  "A chart of price against use, plans as steps", "One line per plan, like a timetable row"]}),
    ("Voice", {
        "loud": ["A legal contract", "A recipe", "A weather forecast", "Sports commentary", "Classified ads",
                 "Museum wall labels", "An assembly manual", "A horoscope", "A field guide", "A boarding pass"],
        "quiet": ["An annual report", "A technical datasheet", "A timetable", "An encyclopedia entry",
                  "A letter from one real person at the company", "Minutes of a meeting", "A style guide",
                  "Release notes", "A scientific abstract: method, result, limits", "A ship's log: dated entries"]}),
    ("Motion", {
        "loud": ["A WebGL shader", "A number counting", "Spinning reels", "Glitch", "Typing, like a terminal",
                 "Parallax that tilts in 3D", "Things that follow the cursor", "A marker moving along a line",
                 "Pages that flip", "Shapes that morph into each other"],
        "quiet": ["Old values struck through as new ones replace them", "Rules that draw themselves once",
                  "Numbers that change only when the data does", "A slow crossfade between two photographs",
                  "Headings that stack at the top as you scroll", "A highlight that sweeps across key words as you read",
                  "A loupe under the cursor that magnifies the small print", "Working that unfolds under a figure on request",
                  "A live clock or date", "A progress rule along one edge"]}),
]
# exactly 10**11 designs per tone
assert len(TRAITS) == 11 and all(len(options[t]) == 10 for _, options in TRAITS for t in TONES)

MOVEMENTS = {
    "quiet": [
        ("Swiss International Style", "an asymmetric column grid, one grotesk, flush left and ragged right, "
                                      "objective photos, no ornament, wide white space"),
        ("Dutch grid modernism, 1960s", "a visible square grid that even the letters follow, lowercase only, "
                                        "one or two flat colours, the structure is the decoration"),
        ("1970s corporate identity manual", "every element specified: grid diagrams, clear-space rules, numbered "
                                            "colour chips, one sans, pages numbered by section (2.1, 2.2)"),
        ("Japanese modernist poster, 1960s", "huge flat shapes in one or two colours, vertical and horizontal type "
                                             "together, a vast empty field"),
        ("Ulm school functionalism", "light grey and white, one small accent colour kept for controls, a fine grid, "
                                     "labels set small in a neutral sans"),
        ("Mid-century scientific journal", "two columns, numbered figures with captions, footnotes, a serif with "
                                           "old-style figures, tables ruled top and bottom only"),
        ("Topographic survey map", "thin precise lines, labels set along the features, a legend, a scale bar, "
                                   "contour tints"),
        ("Raw HTML web, 1996", "default elements, blue underlined links, Times, rules and tables for layout, "
                               "no decoration at all"),
        ("1980s annual report", "full-bleed photographs, small text in narrow columns, thin-line charts with one "
                                "highlight colour, a lot of white"),
        ("Private press book", "a page in classical proportions with wide margins, a strong serif, red initials, "
                               "one woodcut-style ornament"),
    ],
    "loud": [
        ("Bauhaus", "primary colours, circle, square and triangle, heavy rules, a sans set in blocks and on diagonals"),
        ("Constructivism", "red, black and cream, diagonal composition, photomontage, heavy sans in blocks, "
                           "arrows and wedges"),
        ("Memphis, 1980s", "clashing pastels and primaries, squiggles, terrazzo and checks, shapes stacked at odd angles"),
        ("Psychedelic poster, 1960s", "lettering that swells to fill its shape, vibrating complementary colours; "
                                      "keep that to the headline and the body readable"),
        ("Punk zine", "photocopied black and white, ransom-note letters, typewriter text, tape, handwritten arrows"),
        ("New Wave typography, 1980s", "type layered at angles, enlarged halftone screens, stepped rules, "
                                       "the grid shown and then broken"),
        ("Art Deco", "black and gold, stepped symmetrical forms, sunbursts, tall geometric capitals"),
        ("Rave flyer, 1990s", "chrome and warped type, acid colour on black, a dense block of small print "
                              "listing everything"),
        ("Op Art", "black and white only, stripes and checks that warp to suggest depth; keep it away from body text "
                   "and still under reduced motion"),
        ("Victorian playbill", "many wood-type faces in one centred stack, every line a new size and weight, "
                               "printer's ornaments and rules"),
    ],
}
assert all(len(MOVEMENTS[t]) == 10 for t in TONES)


def roll(tone="loud", keep=()):
    """Return the six drawn numbers, the picked one, and its (trait, option) pairs; kept traits are locked."""
    drawn = [f"{secrets.randbelow(10 ** len(TRAITS)):0{len(TRAITS)}d}" for _ in range(6)]
    picked = secrets.choice(drawn)
    return drawn, picked, [(name, LOCKED if name in keep else options[tone][int(d)])
                           for (name, options), d in zip(TRAITS, picked)]


def library(page):
    """Return (id, name) for every specimen on library/<page>.html."""
    specs = [(i, html.unescape(n)) for i, n in SPEC.findall((LIBRARY / f"{page}.html").read_text(encoding="utf-8"))]
    assert len({i for i, _ in specs}) == len(specs), f"duplicate specimen id on library/{page}.html"
    return specs


def check_pointers():
    """Every option that names a specimen (library/layouts.html#lay-01) must point at one that exists."""
    for path, sid in {m for _, o in TRAITS for t in TONES for x in o[t] for m in POINTER.findall(x)}:
        assert sid in dict(library(Path(path).stem)), f"roll table points at missing {path}#{sid}"


def main():
    if LIBRARY.is_dir():
        check_pointers()
    names = [name for name, _ in TRAITS]
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])

    def trait(word):
        match = [n for n in names if n.lower().startswith(word.strip().lower())]
        if not word.strip() or not match:
            parser.error(f"unknown trait {word!r}; pick from: " + ", ".join(names))
        return match[0]

    parser.add_argument("--count", type=int, default=1, help="how many designs, movements or specimens (default 1)")
    parser.add_argument("--tone", choices=TONES, default="loud",
                        help="loud: strange on purpose (default); quiet: unusual but credible for serious products")
    parser.add_argument("--keep", default="", help="comma-separated traits the brand already owns, e.g. colour,type")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--trait", help="roll one option for a single trait: " + ", ".join(names))
    mode.add_argument("--movement", action="store_true", help="roll a design movement to follow, in the chosen tone")
    mode.add_argument("--library", choices=sorted(p.stem for p in LIBRARY.glob("*.html")),
                      help="roll distinct specimens from one page of library/")
    args = parser.parse_args()
    keep = {trait(w) for w in args.keep.split(",")} if args.keep else set()
    if args.library:
        specs = library(args.library)
        if not 1 <= args.count <= len(specs):
            parser.error(f"--count must be 1 to {len(specs)} for library/{args.library}.html")
        for sid, name in secrets.SystemRandom().sample(specs, args.count):
            print(f"{sid} {name}  (library/{args.library}.html#{sid})")
        return
    if args.movement:
        if not 1 <= args.count <= len(MOVEMENTS[args.tone]):
            parser.error(f"--count must be 1 to {len(MOVEMENTS[args.tone])} for --movement")
        for name, rules in secrets.SystemRandom().sample(MOVEMENTS[args.tone], args.count):
            print(f"Movement ({args.tone}): {name}\n  Follow its rules: {rules}")
        return
    if args.trait:
        name = trait(args.trait)
        options = dict(TRAITS)[name][args.tone]
        print(f"{name} ({args.tone}): {secrets.choice(options)}")
        return
    if args.count < 1:
        parser.error("--count must be 1 or more")
    for _ in range(args.count):
        drawn, picked, spec = roll(args.tone, keep)
        print(f"Design {picked}  ({args.tone}; drawn: {' '.join(drawn)})")
        for name, option in spec:
            print(f"  {name}: {option}")


if __name__ == "__main__":
    main()
