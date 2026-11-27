# Eval run: AntiDesign 1.5.0, 2026-11-27

Briefs 1 (Halden Mutual) and 3 (Brasa Nove) from `evals/README.md`, plus one control page for Halden made without the skill. Each brief was designed by a fresh agent that had not seen the skill being written and was not shown the rubric. The skill's author scored the pages, so read the scores with that bias in mind.

## How it was measured

- **Skeleton:** `scripts/skeleton.py` on every page, screenshotted at 1280px and 390px beside the page itself.
- **Headless Chrome (DevTools protocol), with network fonts:**
  - console errors and failed self-checks
  - page-level overflow
  - fonts that failed to load
  - text contrast against solid backgrounds
  - controls without an accessible name
  - type sizes and colours in use
  - endlessly looping animations under emulated reduced motion
- **WebKit (Safari's engine, offscreen):** console errors, overflow and fonts at both widths.
- **Truth:** the page text and source were checked against every fact, price and word-for-word line in the brief, and for the gated feature.

## Scores

Each rubric line is scored 0 to 2; the top total is 18.

| Design | Tone and move | Skeleton | Traits | 5 s | Truth | Access | Function | Craft | Tone | Fresh | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Halden 1: the abstract, filed as a form | quiet, roll, `--keep colour` | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **17** |
| Halden 2: savings passbook | quiet, domain artifact | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** |
| Halden 3: Memphis in one green | loud, movement | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** |
| Brasa 1: thermal fire, check-in, team sheet | loud, roll | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** |
| Brasa 2: topographic survey map | quiet, movement | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** |
| Brasa 3: a proof that reads upward | loud, data draws + invert | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** |
| Control: Halden without the skill | (none) | 0 | 0 | 2 | 2 | 2 | 2 | 1 | 2 | n/a | **11 / 16** |

The control is the default, block for block:
- a nav bar
- a headline beside a rates panel
- a stats strip
- two cards
- a coloured band
- an icon in a rounded box
- an FAQ accordion
- a footer of link columns

It is clean and accessible, with no contrast failures and no errors, but it uses 18 type sizes and 8 colours. Every skill design used 3 to 5 sizes and 2 to 3 colours. No page had a contrast failure, an unnamed control, a console error, page-level overflow, a font that failed to load, or an endless animation under reduced motion. That held in Chrome and in WebKit.

## What failed or nearly failed

- **Halden 1, skeleton (1):** its navigation, "a ruler along the top edge", reads in the skeleton as a bar of links across the top, which is the default shape. It also keeps the vertical reading direction, so it sits exactly at the two-kept limit.
- **Halden 1, motion:** the designer noticed that the quiet motion option "None, on purpose" *is* the default "None", and broke it with a hard cut instead.

## Skill fixes made from this run

- Three quiet roll options built plainly as the default were replaced in `scripts/roll.py`:
  - "None, on purpose" became "Old values struck through as new ones replace them".
  - "A ruler along the top edge" became "A ruler down the left edge".
  - "A strict 12-column grid" became "An asymmetric grid, everything flush left of centre".
- **lay-08 Ring (library):** its items flew out from the top on every page load, and stayed stacked where transitions don't run. They are now placed before transitions switch on.

## Observations, not failures

- **Brand lock against a movement (Halden 3):** Memphis demands clashing colour, but the brand locks colour to one green. The designer followed the skill (the lock wins) and carried the clash in pattern instead of colour. A future roll could skip colour-led movements when colour is locked.
- **Self-checks:** both designers re-cut a page after their own skeleton test (Halden 1, Brasa 2). The test changed the work, which is what it is for.
- **Tone mixing:** both batches mixed tones as the skill asks (Halden quiet, quiet, loud; Brasa loud, quiet, loud). Each brief's off-tone design still scored full marks.
- **Truth details:**
  - Brasa 3's headline claim (68 = 9 + 11 + 16 + 24 + 8) is true.
  - "Closed Sunday and Monday" follows from the brief's hours.
  - The Halden designs label their £1,000 worked example as illustrative.
- **Cost:** each designer took 23 to 29 minutes and about 65 tool calls for three pages.

## Not checked

- Screen readers.
- Real phones and touch on the eval pages.
- Firefox, which isn't installed here.
- Text over Brasa 1's moving WebGL wash and Halden 3's terrazzo pattern: the contrast check skips image and canvas grounds, so these were only checked by eye in screenshots.
- WebKit screenshots of the eval pages; only their errors and overflow were checked.
