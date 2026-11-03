# herdr-critters

A Herdr desktop app mod: the Agents sidebar as cards with a critter for each
agent. The look is a theme: retro pixel art, an Edo woodblock print or glossy
Y2K.

- One card per agent: a sprite, the agent's name with its status box (the
  theme's word, for example `IDLE`, `BUSY`, `HELP!`, `DONE` in retro) beside
  it, and the session name under it (else the tab).
- Every agent gets a name from a list of 30 (4 to 7 letters, `names` in the
  theme), kept across restarts and never two the same. Each name is a
  character with its own sprite.
- Each sprite has one picture per status: idle (eyes shut), working (a bolt),
  blocked (a `!` and a sweat drop), done (happy eyes and a check). The sprite
  box background and border follow the status too.
- Cards are grouped by machine or by space: click `BY MACHINE` / `BY SPACE` in
  the panel header. Each group header shows `busy/total`. A space header uses
  the space's color from the Spaces list.
- The corner badge moves: `z` when idle, a spinner when working, a blinking `!`
  when blocked, a check when done. Working sprites bob.
- Click a card to focus its pane. Hover to pin or unpin.
- A narrow sidebar (under 160 px) shows only the sprite boxes.
- The look is a theme (see [Themes](#themes)). The header button next to
  `BY MACHINE` shows the active theme (`RETRO`); click it to switch to the next.

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

## Themes

Four themes ship. Each has its own names and critters (30, or 12 in noir), colors,
scenes, status words and fonts.

| Theme | Look | Status words | Fonts |
| --- | --- | --- | --- |
| `retro` (default) | Dark pixel arcade: pixel critters, a dusk sky over bricks. | `IDLE` `BUSY` `HELP!` `DONE` | Silkscreen, VT323 |
| `edo` | An ukiyo-e woodblock print on washi paper: Japanese food and objects as vector critters with an ink outline. | `IDLE` `BUSY` `HELP!` `DONE` | Shippori Mincho, Yuji Syuku |
| `y2k` | Glossy Aqua, about 2000 to 2005: vector critters with a white shine, a wallpaper sky over green hills, a light silver panel. | `BRB` `SYNC` `OMG!` `W00T` | Orbitron, Share Tech Mono |
| `noir` | A 1940s detective city at night: 12 pixel critters in costume, all grays with one blood red, rain over cobbles. | `QUIET` `SNOOP` `HEAT!` `SOLVED` | Silkscreen, VT323 |

### How theming works

A theme is data. `main.js` draws the view and reads every color, word, font,
name and art path from the active theme object. It never hard-codes a look.

- `themes/<id>/theme.js` holds the data (see `RECIPE.md` `## Themes` for the
  keys).
- `themes/<id>/art/` holds the SVGs the view shows: the sprites, scenes and
  icons.
- `themes/index.js` lists the themes. The header button cycles through them.

Everything look-related lives in `mods/herdr-critters/themes/<id>/`:

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
    y2k/              same layout
    noir/          same layout
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
   `icon-dither.svg`). Make them with an art package (see [Art](#art)).
3. Import it in `themes/index.js` and add it to `THEMES`. The order is the
   cycle order of the header button.

## Art

`art/generate.py` writes a theme's SVGs to `mods/herdr-critters/themes/<id>/art/`
from the Python package `art/themes/<id>/`. A package draws in one of two ways:

- **Pixel grids** (retro, noir): the package exports ASCII grids, one character per
  pixel, and per-status poses. The engine turns them into SVG and adds the
  status marks. See the `generate.py` docstring for the names a package exports.
- **Vector** (edo, y2k): the package sets `VECTOR = True` and draws the SVG
  text itself: `SPRITES` maps a name to a function of the status, and `SCENES`
  and `ICONS` map a name to SVG text. Each vector package has a `kit.py` with
  one face engine, so every critter poses the same way. Edo draws woodblock
  shapes with an ink outline. Y2k draws glossy bodies with a white shine: a
  `Critter` gives its body and face position, and the kit adds the eyes, mouth,
  blush and status marks.

Edit the art, then:

```sh
uv run --no-project art/generate.py --theme <id>     # default: retro
./install.sh
```

`art/preview.py` draws a sheet of every sprite in every pose
(`art/preview-sprites.png`). Vector themes also need resvg:

```sh
uv run --no-project --with pillow art/preview.py --theme retro
uv run --no-project --with pillow --with resvg-py art/preview.py --theme y2k out.png
```

## Fonts

Retro and Noir use Silkscreen and VT323. Edo uses Shippori Mincho and Yuji Syuku, cut
to the Latin letters with `pyftsubset` so the files stay small. Y2k uses
Orbitron and Share Tech Mono. All are under the SIL Open Font License (see
`mods/herdr-critters/fonts/LICENSE-*.txt`).
Herdr loads them from the mod's `fonts/` folder.

## Limits

- The palette is fixed per theme. It does not follow the Herdr theme.
- Past 30 agents, names repeat with a number (`pixel 2`) and share a sprite.

## Thanks

Kudos to [typecraft](https://x.com/typecraft_dev/status/2117399278197108821)
for the inspiration.
