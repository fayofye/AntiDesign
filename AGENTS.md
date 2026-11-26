# Guide for agents working on this repo

AntiDesign (skill id `antidesign`) is an agent skill: `SKILL.md` is the prompt, `scripts/roll.py` rolls designs, `elements/` holds self-contained demo pages and `references/elements.md` says when to use them. `library/` holds smaller specimens (buttons, motion, heroes, type) listed in `references/library.md`. There is no build step.

## Keep it portable

The skill must work in any agent that reads `SKILL.md` (Claude Code, Codex, Grok Build, Cursor, Gemini CLI and others), and pasted into a plain chat.

- Never name one agent's tools in `SKILL.md`. Write "run", "read" and "ask the user", not a specific tool name.
- `scripts/roll.py` uses the Python standard library only. Elements use plain HTML, CSS and JavaScript with no build and no package.
- Paths in `SKILL.md` are relative to the skill's folder.

## Keep these in step

- **Version:** the same version in `SKILL.md` (`metadata.version`), `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`.
- **Description:** the manifests and `agents/openai.yaml` use the first sentence of the `SKILL.md` description.
- **Traits:** the ten traits in `SKILL.md`'s default table and in `scripts/roll.py` stay the same, in the same order.
- **Elements:** every file in `elements/` has a row in `references/elements.md` and in the README.
- **Library:** every specimen in `library/` has a row in `references/library.md`, and the README's specimen counts match. Keep each specimen's tag exactly `<article class="spec" id="btn-01" data-name="Name">`, with ids sequential per page: `roll.py --library` reads it.

## Before publishing

```bash
python3 scripts/roll.py --count 2
python3 scripts/roll.py --trait colour
python3 scripts/roll.py --library buttons --count 3
npx skills add . --list
```

Open any element or library page you changed in a browser at phone and desktop widths and check the console for errors.
