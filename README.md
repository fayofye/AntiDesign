# anti-default-design

A skill for Claude Code (and other agents that read `SKILL.md` skills) that designs web pages the model would never make on its own.

A model's first design is its most probable one: a centred hero, a gradient, three feature cards, three pricing cards with the middle one highlighted. This skill makes the agent write that default down first, trait by trait, then move away from it on purpose with four moves:

1. **Invert** every trait of the default, past the first opposite that comes to mind.
2. **Let the data draw**: the layout is the product's own numbers (blocks sized by value, copy riding a chart line, a hero that is the calculation).
3. **Become a domain artifact**: the page is an object the product's world already trusts, such as a banknote, a bond coupon, a ledger, a boarding pass or a field guide.
4. **Roll** ten traits from a table of ten billion unusual combinations and build exactly what comes out.

Every design ends with a table of the ten traits marked kept or broken; fewer than eight broken means it isn't done. Four things stay fixed: real facts (sample figures are labelled and add up), accessibility, pages that work on phones, and no copying of real brands.

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

## Install

As a Claude Code plugin:

```
/plugin marketplace add fayofye/anti-default-design
/plugin install anti-default-design@anti-default-design
```

Or as a personal skill, available in every project:

```bash
git clone https://github.com/fayofye/anti-default-design ~/.claude/skills/anti-default-design
```

## Use

Ask for it in your own words, for example "design three unconventional landing pages for this product, nothing templated", or name the skill directly.

To roll designs yourself:

```bash
python3 scripts/roll.py --count 3
python3 scripts/roll.py --trait colour
```

```
Design 1014730075  (drawn: 3319805863 9272279496 9326594069 1014730075 1141958003 1544821760)
  Reading direction: One screen, no scroll; content swaps in place
  Layout: Blocks sized by the product's own numbers
  Hero: A form you fill before you see anything
  Components: Index tabs down one edge
  Type: Comic Neue against Times
  Colour: Thermal camera
  Texture: Halftone dots
  Pricing: Blocks sized by price
  Voice: A horoscope
  Motion: Parallax that tilts in 3D
```

Python 3.8 or later, standard library only. The elements need only a browser.

## License

MIT
