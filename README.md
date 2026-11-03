# herdr-critters

A Herdr desktop app mod: the Agents sidebar as retro pixel cards.

- One card per agent: a pixel sprite, the agent's name with its status box
  (`IDLE`, `BUSY`, `HELP!`, `DONE`) beside it, and the session name under it
  (else the tab).
- Every agent gets a name from a list of 30 (4 to 7 letters, `NAMES` in
  `main.js`), kept across restarts and never two the same. Each name is a
  character with its own sprite.
- Each sprite has one picture per status: idle (eyes shut), working (a yellow
  bolt), blocked (red eyes, a red `!`, a sweat drop), done (happy eyes, a green
  check). The sprite box background and border follow the status too.
- Cards are grouped by machine or by space: click `BY MACHINE` / `BY SPACE` in
  the panel header. Each group header shows `busy/total`. A space header uses
  the space's color from the Spaces list.
- The corner badge moves: `z` when idle, a spinner when working, a blinking `!`
  when blocked, a check when done. Working sprites bob.
- Click a card to focus its pane. Hover to pin or unpin. Sub-agents show as
  small rows under their parent; click one to peek.
- A narrow sidebar (under 160 px) shows only the sprite boxes.

![Herdr critters](preview.png)

## Install

Ask your Herdr agent:

> Add herdr.dev/layouts/izerozlu/herdr-critters

It copies `layouts/critters.json` and `mods/herdr-critters/` into
`~/.config/herdr-app/`, runs `herdr-app check` and switches to the `critters`
layout. `ctrl-shift-l` switches back to your own layout.

To use only the mod in a layout of your own, set that layout's agents block to
`"content": { "mod": "herdr-critters" }`.

## Develop

```sh
./install.sh
```

This copies `mods/herdr-critters` to `~/.config/herdr-app/mods/` and runs
`herdr-app check`. Herdr reloads the mod live. Run it again after every change.
A symlink does not work: Herdr does not load a mod's images through one.

`RECIPE.md` is the brief another agent builds the mod from. Update it and
`preview.png` when the mod changes.

## Art

The sprites, scenes and icons are ASCII grids in `art/generate.py` and
`art/sprites/batch_*.py`. `art/preview.py` draws a sheet of them
(`art/preview-sprites.png`). Edit a grid, then:

```sh
uv run --no-project art/generate.py
./install.sh
```

## Fonts

Silkscreen and VT323, both under the SIL Open Font License (see
`mods/herdr-critters/fonts/LICENSE-*.txt`). Herdr loads them from the mod's
`fonts/` folder.

## Limits

- The palette is fixed. It does not follow the Herdr theme.
- Past 30 agents, names repeat with a number (`pixel 2`) and share a sprite.

## Thanks

Kudos to [typecraft](https://x.com/typecraft_dev/status/2117399278197108821)
for the inspiration.
