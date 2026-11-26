# Elements

Each file in `elements/` is one self-contained HTML page: open it, read it, copy the parts you need. All of them respect `prefers-reduced-motion`, use real buttons and labelled inputs, and show sample copy marked as sample. Replace every sample figure and line with the product's own.

| Element | File | Use it when | Change before use |
|---|---|---|---|
| 3D liquid, 180 models | `liquid-3d.html` | A fintech or luxury page needs a hero that feels expensive and alive | Pick a model number; set the palette to the product's colours; put a dark gradient under the copy for contrast |
| Security print | `security-print.html` | A bank, payments or ledger product, where trust is the point | The serial, the corner values, the microtext string and the coupon contents |
| Neon and counting number | `neon.html` | One figure is the story and the page can be loud | `data-count-to`, the tube words, the halftone colours |
| Copy on a data line | `flow-text.html` | The product has a series that tells a story (an equity curve, usage, growth) | `values`, `text`, `marks`; keep the text short enough to stay large |
| Commentary quiz | `quiz.html` | The product's value is a surprise the visitor can guess at | `QUIZ`: questions with true answers from the product's facts |
| Slot machine | `slot-machine.html` | Choosing among plans, sizes or scenarios can be a game | `REELS` and `result()`; every result must be true or labelled sample |
| Money map | `money-map.html` | One amount splits into parts and the split is the message | `PARTS`: labels, values and colours |

## 3D liquid models

One parametric shader makes all 180: model `n` uses form `n % 6`, material `floor(n / 6) % 6` and palette `floor(n / 36)`.

- Forms: Sheet, Ripples, Blobs, Satin, Droplets, Vortex.
- Materials: Chrome, Glass, Oil slick, Ink, Gel, Mercury.
- Palettes: Silver, Ultraviolet, Aqua, Ember, Rose.

Open `liquid-3d.html#62` to see model 62, or step through them with its buttons. To embed one, copy `FRAG`, `describe()` and `mountLiquid(canvas, n)`. It draws at 60% resolution and stops animating under reduced motion. Without WebGL it returns `null`, and whatever sits behind the canvas (keep a CSS gradient there) stands in.

## Watch out

- **Fonts.** The neon, stencil, Six Caps, Bodoni and Anybody looks need their web fonts. Offline previews fall back to system fonts and lose the effect; self-host for anything that ships.
- **Flow text.** `flowLine()` shrinks the type until the sentence fits the line. Very long copy ends up small, so cut the copy instead.
- **Quiz and slot machine.** Their outcomes are claims. Use the product's real rules, or say plainly that the numbers are invented.
