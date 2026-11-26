# anti-default-design

A skill for Claude Code (and other agents that read `SKILL.md` skills) that designs web pages the model would never make on its own.

A model's first design is its most probable one: a centred hero, a gradient, three feature cards, three pricing cards with the middle one highlighted. This skill makes the agent write that default down first, then move away from it on purpose, with four moves:

1. **Invert** every trait of the default.
2. **Let the data draw**: the layout is the product's own numbers (blocks sized by value, copy riding a chart line, a hero that is the calculation).
3. **Become a domain artifact**: the page is an object the product's world already trusts, such as a banknote, a bond coupon, a ledger, a boarding pass or a field guide.
4. **Roll** from a table of a million unusual combinations and build exactly what comes out.

It keeps four things fixed: real facts (sample figures are labelled and add up), accessibility, pages that work on phones, and no copying of real brands.

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
```

```
Design 547788  (drawn: 769833 527644 873458 251705 547788 360076)
  Structure: A stack of cards you flip
  Type: Stencil (Big Shoulders Stencil)
  Colour: Vaporwave pink and cyan
  Hero: A slot machine
  Texture: Hard offset shadows
  Voice: A field guide
```

Python 3.8 or later, standard library only.

## License

MIT
