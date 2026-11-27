# Halden Mutual: three designs with AntiDesign 1.5.0

Product facts used, and nothing else: easy-access saver 3.10% AER variable; 95-day notice saver 3.60% AER variable; no fees; open with £1; member-owned since 1874; 41 branches. The line "Halden Mutual is owned by its members, not by shareholders." appears word for word in all three. Joint accounts (gated) appear nowhere.

Brand lock: colour (Halden green `#1F4D3A` on white). No logo or typeface was given, so only colour is locked.

Illustrative figures are the same in every design: £1,000 kept 12 months, rate unchanged, nothing taken out → £31.00 (easy access), £36.00 (95-day notice), £5.00 apart. Each page labels them illustrative and runs a load-time `console.assert` on the sums.

## The default I would have made (section 1)

| Trait | My default for Halden Mutual |
|---|---|
| Reading direction | Vertical scroll, left to right |
| Layout | Centred container, stacked sections: hero, two accounts, "why mutual", FAQ, footer |
| Navigation | Wordmark left, Savings / About / Branches, "Open an account" button far right; footer link columns |
| Hero | Eyebrow pill "Member-owned since 1874", headline "Savings that belong to you", subhead, two buttons, a photo of a family or a phone |
| Components | Two account cards with icons in rounded squares, "Open in 3 steps", an FAQ accordion |
| Type | Serif display over a sans |
| Colour | Locked green on white (otherwise cream with a clay accent) |
| Texture | Soft shadows on the cards |
| Pricing | Two rate cards side by side, the notice saver highlighted |
| Voice | Calm product marketing: "Your money, working for you" |
| Motion | Fade-ins on scroll |

## Design 1: The abstract, filed as a form

- **Tone:** quiet (a bank holds money).
- **Move:** Roll (5), with `--keep colour`.
- **Roll output (verbatim):**

```
$ python3 scripts/roll.py --tone quiet --keep colour
Design 39706180380  (quiet; drawn: 14027201884 39706180380 22285397762 27850003900 39638533558 88049508168)
  Reading direction: One sentence per screen, read in order
  Layout: A form: numbered boxes, all the content inside them
  Navigation: A ruler along the top edge, sections as its marks
  Hero: The one key figure, set huge and still, its working shown small
  Components: Small-caps labels over plain paragraphs, no boxes at all
  Type: Monospace only (Spline Sans Mono)
  Colour: Locked: build it from the brand
  Texture: Hairline rules, nothing else
  Pricing: Dotted leaders to each price, like a contents page
  Voice: A scientific abstract: method, result, limits
  Motion: None, on purpose: every change is instant
```

- **How the roll was built:** seven sheets (Result, Background, Method, Rates, Comparison, Limits, Conclusion), one sentence each, each a grid of numbered form boxes (1.1, 1.2 …) with struck-through "left blank" boxes. Layout says boxes and components say "no boxes": settled as boxes being the form itself, with only small-caps labels and plain paragraphs inside them. "Motion: none" built plainly would be the default, so the page has state that changes by hard cut: tick an account box or type an amount and the huge figure and its working change at once, with no transition. The figure breaks out across the form's left edge, the one break in the grid.
- **Element / library:** none.

| Trait | Status | Note (judged on the skeleton) |
|---|---|---|
| Reading direction | **kept** | Still a vertical scroll; the one-sentence pacing doesn't change the shape |
| Layout | broken | Full-bleed form grid of numbered boxes in varying sizes, struck-through blanks; no centred container |
| Navigation | **kept** | The rolled ruler is still a bar of links across the top in the skeleton |
| Hero | broken | One huge figure, its working beside the finding; no pill, no picture, one link |
| Components | broken | Small-caps labels over paragraphs; no cards, icons, steps or accordions |
| Type | broken | Spline Sans Mono only |
| Colour | locked | Green on white, nothing else |
| Texture | broken | Hairlines only; no shadow, glow or blur |
| Pricing | broken | Dotted leaders, like a contents page |
| Voice | broken | Scientific abstract: background, method, result, limits, conclusion |
| Motion | broken (weakest call) | Deliberate instant cuts driven by the tick boxes and the amount field; no fades |

Kept: 2, at the limit.

## Design 2: The passbook

- **Tone:** quiet.
- **Move:** Become a domain artifact (3): a savings passbook, plus its opening slip with a counterfoil.
- **Roll output:** none (no roll was used for this design).
- **Craft details:** cloth-weave cover with a blind-embossed HM 1874 seal and a paper label window; running heads and folios; ledger with a double rule before the money columns; "nil" in the fees row; clerk's handwriting for the particulars; ruled blank lines below the entries; a "Specimen · illustrative figures" rubber stamp; stitched spine; hard page-block edges; thumb index cut into the fore-edge; a perforated counterfoil that echoes the slip as you fill it.
- **Element / library:** none.

| Trait | Status | Note (judged on the skeleton) |
|---|---|---|
| Reading direction | broken | Pages turn sideways inside the book, one spread on desktop and one page on phone; the window doesn't scroll on desktop |
| Layout | broken | One object (the book) and a slip on an empty counter |
| Navigation | broken | Thumb index on the book's fore-edge, plus Previous/Next; no top bar, no footer |
| Hero | broken | The passbook cover with a rate label window and one link |
| Components | broken | Ledger tables, rubber stamps, a rulebook in roman articles, the slip with its counterfoil |
| Type | broken | Old Standard TT (Victorian modern) for everything, Cedarville Cursive for the clerk's entries; no sans |
| Colour | locked | Green cloth, green ink, white paper |
| Texture | broken | Cloth weave, a printed wave safety tint, hard page edges; no soft shadow or blur |
| Pricing | broken | Rates live in each account's ledger terms and its interest entry |
| Voice | broken | Rulebook articles ("Either account may be opened with £1") and ledger terseness |
| Motion | broken | Rubber stamps thump down as a page opens; pages slide; none under reduced motion |

Kept: 0.

## Design 3: Memphis, in one green

- **Tone:** loud (the batch's other tone).
- **Move:** Borrow a movement (4).
- **Roll output (verbatim):**

```
$ python3 scripts/roll.py --movement --tone loud
Movement (loud): Memphis, 1980s
  Follow its rules: clashing pastels and primaries, squiggles, terrazzo and checks, shapes stacked at odd angles
```

- **Conflict with the lock:** the movement's colour rule (clashing pastels and primaries) would override the locked brand colour, and the skill says a move never overrides a lock. So the clash is carried by pattern (terrazzo against checks, stripes, zigzags and squiggles), all in Halden green on white. I did not reroll the movement.
- **How it follows the other rules:** sections are shapes stacked at odd angles in a pile. Pulling one (plain `#links`, swapped by CSS `:target`, so it works without JS) swings it to the top. The page is one screen and never scrolls. Figures are set in Titan One filled with stripes. Shape tokens (circle, triangle, half-moon, zigzag, checks) are the navigation.
- **Element / library:** none.

| Trait | Status | Note (judged on the skeleton) |
|---|---|---|
| Reading direction | broken | One screen that never scrolls; sections swap in place out of a pile |
| Layout | broken | A pile of tilted slabs on a terrazzo ground; no container or stacked sections |
| Navigation | broken | Pile of shape tokens, a column on desktop and a row on phone; the wordmark sits on its own tilted slab |
| Hero | broken | The verbatim sentence across three tilted pieces, two rate stickers and one pill link; no pill, no subhead, no picture |
| Components | broken | Slabs with checks, zigzag and striped edges; bare shape tokens; stickers |
| Type | **kept** | Rounded display sans over a geometric sans body is close to the "display over body" default; only the striped figures move away from it |
| Colour | locked | Green on white; Memphis clash moved into pattern |
| Texture | broken | Terrazzo, checks, stripes, squiggles, hard offset shadows |
| Pricing | broken | Two striped figures in a staggered, tilted stack inside one slab |
| Voice | broken | Short and playful: "Pick one. Put in £1. Done.", "pull a shape" |
| Motion | broken | Pulled slab swings to the top with an overshoot; none under reduced motion |

Kept: 1.

## Batch check (no choice in two designs)

Every trait choice differs across the three designs. Colour is the same in all three because it is locked. Two possible near-overlaps: both design 2 (page-block edges) and design 3 (wordmark and sticker shadows) use hard offset outlines; and design 2's ledger ruling is made of hairlines, which are design 1's whole texture.

## What was checked

- Screenshots in Chromium at 1280×800 and 390×844 for all three; fixes made after the first pass (book width, ledger columns, a 1330px phone overflow from hidden captions in design 2; clipped striped figures, a viewport scroll on hash change, and a `:target` specificity bug in design 3).
- Skeletons for all three via `scripts/skeleton.py` (copies deleted afterwards).
- Console: no errors, no failed asserts on any page.
- Fonts loaded from Google Fonts in this preview; tabular figures confirmed for Old Standard TT.

## Not checked

- `prefers-reduced-motion` was not emulated; reduced-motion paths were reviewed in code only.
- Offline font fallback was not viewed (the preview had network).
- Real devices, Safari/iOS and Firefox; screen readers; a full keyboard-only walkthrough.
- All "Open an account" targets point to the placeholder `/open`.
