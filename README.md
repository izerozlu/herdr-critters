# herdr-critters

A Herdr desktop app mod: the Agents sidebar as retro pixel cards.

- One card per agent: a pixel sprite, the agent's name with its status box
  (`IDLE`, `BUSY`, `HELP!`, `DONE`) beside it, and the session name under it
  (else the tab).
- Every agent gets a name from a list of 30 (4 to 7 letters, `names` in the
  theme), kept across restarts and never two the same. Each name is a
  character with its own sprite.
- Each sprite has one picture per status: idle (eyes shut), working (a yellow
  bolt), blocked (red eyes, a red `!`, a sweat drop), done (happy eyes, a green
  check). The sprite box background and border follow the status too.
- Cards are grouped by machine or by space: click `BY MACHINE` / `BY SPACE` in
  the panel header. Each group header shows `busy/total`. A space header uses
  the space's color from the Spaces list.
- The corner badge moves: `z` when idle, a spinner when working, a blinking `!`
  when blocked, a check when done. Working sprites bob.
- Click a card to focus its pane. Hover to pin or unpin.
- A narrow sidebar (under 160 px) shows only the sprite boxes.
- The look is a theme. The header button next to `BY MACHINE` shows the active
  theme (`RETRO`); click it to switch to the next one. Two themes ship: `retro`
  (dark pixel critters) and `edo` (an ukiyo-e print on washi paper, with
  Japanese food and objects as the critters).

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

`art/generate.py` is the engine; each theme's art lives in `art/themes/<id>/`.
Retro's sprites, scenes and icons are ASCII grids. Edo is a vector theme: its
package draws the SVG itself (woodblock shapes with an ink outline, see
`art/themes/edo/kit.py`). The SVGs go to `mods/herdr-critters/themes/<id>/art/`.
`art/preview.py` draws a sheet of them (`art/preview-sprites.png`; a vector theme
needs `--with resvg-py`). Edit the art, then:

```sh
uv run --no-project art/generate.py --theme retro
./install.sh
```

`--theme` defaults to `retro`.

## Themes

Everything look-related lives in `mods/herdr-critters/themes/<id>/`. `main.js`
reads only theme data.

```
mods/herdr-critters/
  main.js
  fonts/              shared by all themes
  themes/
    index.js          registry (THEMES, DEFAULT_THEME, themeById)
    retro/
      theme.js        colors, scenes, status words, names, fonts, art path
      art/            the SVGs
    edo/              same layout
```

The chosen theme id is shared state (`herdr-critters.theme`). A missing or
unknown id falls back to `retro`. Retro keeps its names in `localStorage` key
`names`; other themes use `names.<id>`.

### Add a theme

1. Copy `themes/retro/theme.js` to `themes/<id>/theme.js`. Change `id`, `label`,
   `art` and the values. Keep every key. `namesKey` is optional: it sets where
   the picked names are stored (default `names.<id>`; retro keeps `names`).
2. Add the art in `themes/<id>/art/` (`sprite-<name>-<status>.svg` for every
   name, `scene-<status>.svg`, `icon-machine-<scene>.svg` for every scene,
   `icon-dither.svg`). Use `art/themes/<id>/` and `generate.py --theme <id>`.
3. Import it in `themes/index.js` and add it to `THEMES`. The order is the
   cycle order of the header button.

## Fonts

Retro uses Silkscreen and VT323. Edo uses Shippori Mincho and Yuji Syuku, cut
to the Latin letters with `pyftsubset` so the files stay small. All are under
the SIL Open Font License (see `mods/herdr-critters/fonts/LICENSE-*.txt`).
Herdr loads them from the mod's `fonts/` folder.

## Limits

- The palette is fixed per theme. It does not follow the Herdr theme.
- Past 30 agents, names repeat with a number (`pixel 2`) and share a sprite.

## Thanks

Kudos to [typecraft](https://x.com/typecraft_dev/status/2117399278197108821)
for the inspiration.
