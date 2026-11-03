# Herdr critters

The Agents sidebar as retro pixel cards. Every agent is a small named critter
with its own sprite, standing in a pixel scene that changes with its status.

![Herdr critters](preview.png)

## What you see

The mod fills the layout's `agents` block, top to bottom:

- **Header** (38 px): a dither icon, `AGENTS` in Silkscreen 11 px `#6b6f82`, a
  `BY MACHINE` / `BY SPACE` toggle (Silkscreen 9 px, 1 px `#34364a` border), a
  theme button beside it (same style, shows the theme label, `RETRO`; click
  cycles to the next theme), and on the right `N BUSY` (cyan `#5ee6f2` when any
  agent works, else gray). The left group shrinks first, the busy count never
  gets cut.
- **Group headers** (30 px): a 15x11 machine icon, the group label in bold
  Silkscreen 11 px, a 2 px rule, and `busy/total`. By machine the label is
  `THIS MACHINE` or the machine name; by space it is the space name in capitals,
  in the space's color from the Spaces list.
- **Cards**, 8 px apart, 10 px side padding: a 2 px border, the scene's card
  color as fill. Left is a 74x62 sprite box; right is the name (VT323 20 px,
  `#f1ecff`) with a status box beside it (Silkscreen 10 px, 1 px border,
  17 px high), and under it the session name (11.5 px, `#9a95b0`).
- **Sub-agents**: 22 px rows under their parent, indented 10 px per level:
  `└`, the name, the status word in Silkscreen 8 px.
- **Empty**: `NO PLAYERS YET` in orange and one line of help.
- **Narrow sidebar** (sidebar under 160 px wide): only 36x30 sprite boxes in a
  column, the focused one with an orange border.

Background `#12131b`. The palette is fixed per theme and does not follow the
Herdr theme. All of it comes from the active theme object (see Themes below).

Scenes by machine: this machine is `dusk` (purple), other machines take `den`
(blue-gray), `dawn` (rust) and `moss` (green) in turn.

## How it behaves

- **Names**: each agent gets a random name from a list of 30 (pixel, byte,
  nova, rook, ziggy, mochi, bolt, echo, juno, kiwi, luma, miso, nimbus, onyx,
  pepper, quill, rusty, sprout, tango, umbra, vega, waffle, yeti, zephyr, comet,
  dusty, fable, gizmo, hopper, ivory). The `edo` theme has its own 30 (onigiri,
  sushi, dango, mochi, ramen, tofu, taiyaki, matcha, gyoza, bento, tempura,
  wasabi, sake, udon, natto, yuzu, miso, senbei, anpan, tamago, kokeshi, daruma,
  chochin, geta, sensu, furin, kendama, torii, kasa, maneki). The pick uses `crypto` random, never two
  the same, and is kept in `localStorage` by agent address across restarts (key
  `names` for retro, `names.<id>` for other themes). Past 30 agents a name
  repeats with a number (`pixel 2`) and shares a sprite.
- **Status**, on the status box, sprite, scene and corner badge:
  - idle: `IDLE` gray, eyes shut, badge `z`/`Z` blinking.
  - working: `BUSY` cyan, a yellow bolt, badge a 4-frame spinner, the sprite
    bobs 3 px.
  - blocked (and error): `HELP!` red, red eyes, a red `!` and a sweat drop,
    badge `!` pulsing, the card border red.
  - done: `DONE` green, happy eyes, a green check, badge `✓`.
- The focused agent's card has an orange `#e8922e` border.
- Click a card to focus its pane (`pane.focus`). Hover shows a pin button; it
  runs `terminal.pin`. Pinned agents go first in their group.
- The group toggle is shared state (`herdr-critters.group`). The theme button
  is shared state too (`herdr-critters.theme`, a theme id; unknown or missing
  means `retro`).
- The mod sets the agent order (`setAgentOrder`) to the order it shows.

## Built from

- **Layout** `layouts/critters.json`: the shipped `main` layout with the
  `agents` block set to `{ "mod": "herdr-critters" }`.
- **Mod** `mods/herdr-critters/`: `main.js` (one `View`, theme-agnostic),
  `mod.json` (`place: none`), `themes/` (registry `index.js` and one folder per
  theme with `theme.js` and `art/`), `fonts/`.
- **herdr functions**: `agents`, `terminals`, `spaces`, `machines`, `layout`,
  `theme`, `shared`, `setShared`, `setAgentOrder`, `run`.
- **Commands**: `pane.focus`, `terminal.pin`, `terminal.peek`.
- **Shipped mods it uses**: the `pin` and `pin-off` icons of
  `workspace-chrome`.
- **Programs, network, files**: none. It does not run programs, reach the
  network or read files outside its own folder.
- **Art**: SVGs in `mods/herdr-critters/themes/<id>/art/`: one sprite
  per name and status (`sprite-<name>-<status>.svg`), a scene per status
  (`scene-<status>.svg`), a machine icon per scene (`icon-machine-<scene>.svg`)
  and `icon-dither.svg`. Made by
  `uv run --no-project art/generate.py --theme <id>` (default `retro`) from
  `art/themes/<id>/`: ASCII grids for retro (pixel art), drawing code for edo
  (vector woodblock prints) and y2k (glossy vector critters). A raster theme
  draws the same files as PNG (`.png` in place of `.svg`) and sets `artExt`:
  noir (black cutout critters, drawn with skia-python; run generate.py with
  `--with pillow --with skia-python`) and deepsea (soft gel critters, drawn with
  skia-python; also `--with imagequant`) and garden (felt craft critters, painted
  with Pillow and numpy; run generate.py with `--with numpy --with pillow`).
- **Fonts**: Silkscreen and VT323 (retro, noir, deepsea, garden), Shippori Mincho and Yuji Syuku cut
  to Latin letters (edo), Orbitron and Share Tech Mono (y2k), all SIL Open Font
  License, in `fonts/`.

## Themes

A theme is `themes/<id>/theme.js`, a default export of one object:

- `id`, `label` (shown on the header button), `art` (art folder path),
  `fonts` (`pixel`, `mono`, optional `monoSize` and `monoLine` for the name
  text, default 20 and `18px`), optional `namesKey` (storage key for names) and
  optional `artExt` (the art files' type, `"svg"` by default, `"png"` for
  raster art).
- `colors`: `bg`, `head`, `machine`, `focus`, `text`, `sub` and the rest the
  view uses (badge, borders, hover, dividers).
- `scenes` (each `card`, `edge`, `box`, `label`), `localScene` and
  `remoteScenes`.
- `status`: `working`, `blocked`, `done`, `idle`, each `{ word, color }`.
- `names`: the 30 agent names; each needs its sprites in `art/`.

`themes/index.js` exports `THEMES` (cycle order), `DEFAULT_THEME` (`retro`) and
`themeById(id)` (unknown id gives the default). To add a theme: write
`theme.js`, add the art, import it in `index.js` and add it to `THEMES`.
