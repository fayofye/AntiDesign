# AntiDesign

A skill for Claude Code (and other agents that read `SKILL.md` skills) that designs web pages the model would never make on its own.

A model's first design is its most probable one: a centred hero, a gradient, three feature cards, three pricing cards with the middle one highlighted. This skill makes the agent write that default down first, trait by trait, then move away from it on purpose with five moves:

1. **Invert** every trait of the default, past the first opposite that comes to mind.
2. **Let the data draw**: the layout is the product's own numbers (blocks sized by value, copy riding a chart line, a hero that is the calculation).
3. **Become a domain artifact**: the page is an object the product's world already trusts, such as a banknote, a bond coupon, a ledger, a boarding pass or a field guide.
4. **Borrow a movement**: follow a rolled design movement's rules to the letter (Swiss International Style, Constructivism, a 1970s identity manual).
5. **Roll** eleven traits from a table of a hundred billion unusual combinations and build exactly what comes out.

Every design takes a tone: **loud** (strange on purpose) or **quiet** (unusual but credible, for a bank, a law firm or B2B software). Traits the brand already owns, such as its colours or typefaces, can be locked so no move overrides them.

Every design is then stripped to its skeleton (fonts, colours and images removed, every box outlined) and held against the default, because a reskinned row of three pricing cards is still a row of three pricing cards. It ends with a table of the eleven traits marked kept, broken or locked; more than two kept means it isn't done. A craft pass (one type scale, at most four colours, tabular figures, a five-second test on a phone) and a desktop and phone screenshot pass follow. Four things stay fixed: real facts (sample figures are labelled and add up), accessibility, pages that work on phones, and no copying of real brands.

## Demo

One product, Propel Audit (a payout desk and trading journal for prop-firm traders), designed both ways. Sample figures in the shots are illustrative.

<table>
<tr>
<th width="33%">Without the skill</th>
<th colspan="2">With AntiDesign</th>
</tr>
<tr>
<td rowspan="2" valign="top" width="33%">
<img src="demo/1-generic-default.jpg" width="270" alt="The default: a dark page with a violet gradient headline, two buttons, a dashboard mockup and a grid of feature cards"><br>
<sub>The default the model makes unprompted</sub><br><br>
<img src="demo/2-generic-bento.jpg" width="270" alt="A bento grid of cream and forest-green tiles with a big kept figure, feature tiles and pricing tiles"><br>
<sub>Rolled from a table of safe options: still generic</sub>
</td>
<td valign="top" width="33%">
<img src="demo/3-fintech-liquid.jpg" width="270" alt="A black page with an iridescent 3D liquid-chrome hero, thin headline and a frosted-glass payout statement"><br>
<sub>Fintech: 3D liquid chrome hero</sub>
</td>
<td valign="top" width="33%">
<img src="demo/4-bank-security-print.jpg" width="270" alt="A banknote-style page with guilloché rosettes, microtext borders, numbered terms and tear-off coupons for pricing"><br>
<sub>Bank: banknote security print</sub>
</td>
</tr>
<tr>
<td valign="top">
<img src="demo/5-colour-blocks.jpg" width="270" alt="A payout split into clashing yellow, blue, pink and orange blocks, each sized by its dollar amount"><br>
<sub>The layout is the money</sub>
</td>
<td valign="top">
<img src="demo/6-field-guide.jpg" width="270" alt="A pink field guide page in stencil type with a slot machine, a stack of species cards and expedition kits"><br>
<sub>Field guide with a slot machine</sub>
</td>
</tr>
</table>

## Elements

Working, self-contained demos in `elements/`, for the agent to re-cut to each product:

| Element | What it is |
|---|---|
| `liquid-3d.html` | A WebGL liquid hero with 180 models: 6 forms × 6 materials × 5 palettes |
| `security-print.html` | Banknote craft: guilloché rosettes and bands generated from sine waves, microtext, lathe-work, coupons |
| `neon.html` | Neon tube type, a number that counts up, a halftone sunset |
| `flow-text.html` | Copy set along a data line that you scroll sideways |
| `quiz.html` | A live-commentary quiz with a scoreboard and glitch type |
| `slot-machine.html` | Reels and a lever that land on an outcome |
| `money-map.html` | One amount split into blocks sized by their dollars, with live inputs |

`references/elements.md` says when to use each one.

## Library

Smaller parts in `library/`: 90 numbered specimens on six pages, each a working mechanism with its own typeface and palette. None of them is a gradient pill, a fade-up on scroll or a centred headline with two buttons.

| Page | Specimens | Examples |
|---|---|---|
| `buttons.html` | 17 | A rubber stamp that inks itself, a ticket stub that tears off, a fuse you hold to burn, a safety cover you lift before you publish |
| `motion.html` | 19 | An odometer, a split-flap headline, words that fall and pile up, a pen plotter, an aperture iris, a thermal receipt fed by scroll |
| `heroes.html` | 13 | A newspaper front page, a crossword, an exploded diagram, a tape measure, a tide chart, a transit line |
| `type.html` | 20 | Letters that melt with the year, a chart inside a sentence, a scannable barcode, words redacted until clicked, text on a spiral |
| `layouts.html` | 10 | One working skeleton per strange reading direction: sideways, columns right to left, bottom to top, zoom to read, a ring, a book whose pages turn |
| `textures.html` | 11 | Halftone and engraved hatching that follow tone, CRT scanlines, torn paper, dither, crop marks, a baseline grid, duotone for the product's own photos |

The agent doesn't pick from them by taste. Layouts and textures are named by the rolled trait; for the rest it rolls for one and re-cuts it to the product:

```bash
python3 scripts/roll.py --library heroes
python3 scripts/roll.py --library buttons --count 3
```

`references/library.md` lists every specimen with when to use it and what to change.

## Install

The skill is plain Markdown plus a standard-library Python script, so it works in any agent that reads `SKILL.md` skills. Leave off `--global` in any `npx skills` command below to install it only in the current project.

### Claude Code

```
/plugin marketplace add fayofye/AntiDesign
/plugin install antidesign@antidesign
```

Or as a personal skill, available in every project:

```bash
git clone https://github.com/fayofye/AntiDesign ~/.claude/skills/antidesign
```

### Codex

```bash
npx skills add fayofye/AntiDesign --global --agent codex
```

Then ask for it by name: `$antidesign`.

### Grok Build

```bash
npx skills add fayofye/AntiDesign --global --agent grok
```

### Cursor, Gemini CLI, GitHub Copilot and other agents

```bash
npx skills add fayofye/AntiDesign --global --agent '*'
```

This installs it for every agent the [Skills CLI](https://github.com/vercel-labs/skills) supports. For an agent it does not know, copy this folder into that agent's skills folder.

### Claude.ai and Claude Desktop

Download this repository as a ZIP (**Code → Download ZIP**) and upload it as a skill in Settings.

### Chat apps without skills (Grok, ChatGPT and others)

Paste `SKILL.md` into the chat or the app's custom instructions. The chat can't run the roll script, so run `python3 scripts/roll.py` yourself and paste the output; the skill tells the agent never to invent a roll. Open the files in `elements/` and `library/` in a browser and attach the ones you want it to adapt.

## Use

Ask for it in your own words, for example "design three unconventional landing pages for this product, nothing templated", or name the skill directly.

To roll designs yourself:

```bash
python3 scripts/roll.py --count 3
python3 scripts/roll.py --count 3 --tone quiet --keep colour,type
python3 scripts/roll.py --movement --tone quiet
python3 scripts/roll.py --trait colour --tone quiet
```

```
Design 47657395644  (loud; drawn: 53686637776 47657395644 83944875551 07045051689 91904639032 20411628849)
  Reading direction: Zoom in to read: each level is closer (library/layouts.html#lay-05)
  Layout: A timeline running off both edges
  Navigation: A departure board listing every section
  Hero: A spotlight under the cursor; the rest is dark
  Components: Notes clipped to a line, at angles
  Type: Worn typewriter (Special Elite)
  Colour: Mid-grey only
  Texture: Dithered gradients (library/textures.html#tex-06)
  Pricing: A price tag on a string
  Voice: Classified ads
  Motion: Typing, like a terminal
```

To strip a page to its skeleton for the check (it writes `page.skeleton.html` beside the page):

```bash
python3 scripts/skeleton.py path/to/page.html
```

Python 3.8 or later, standard library only. The elements need only a browser.

## Evals

`evals/README.md` holds five invented product briefs (a bank, B2B software, a restaurant, a charity, a developer tool) and a scoring rubric. Run them in fresh sessions with and without the skill before each release, and log the scores there.

## License

MIT
