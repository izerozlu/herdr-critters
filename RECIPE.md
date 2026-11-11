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
- **Group headers** (30 px): a 12 px chevron (down when open, right when
  collapsed), a 15x11 machine icon, the group label in bold
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
- Click a group header to collapse the group: its cards go and only the
  header line stays. The collapsed groups are shared state
  (`herdr-critters.collapsed`, a map of `space:<id>` or `machine:<name>` to
  `true`).
- Hover also shows a minus button beside the pin: it makes the card compact,
  one line with a 36x30 sprite box, the name and the status box (a plus button
  opens it again). Compact cards are shared state (`herdr-critters.compact`, a
  map of agent address to `true`).
- Right-click a card (or a small sprite box) for a menu: `PIN TO TOP` /
  `UNPIN`, `COLLAPSE PANE` / `EXPAND PANE`, `COLLAPSE CARD` / `EXPAND CARD`
  (not on a collapsed pane's card), `COLLAPSE GROUP` / `SHOW GROUP` (the
  agent's own group). It is a pointer popup (`openOverlay`, `kind: popup`,
  `frame: none`, 190x118) of this same mod with `props().menu` set to the
  agent's address; it draws in the theme's colors and closes on a pick.
- A collapsed pane's agent stays as a compact card; a click puts the pane
  back (see [Pane collapse](#pane-collapse)).
- The group toggle is shared state (`herdr-critters.group`). The theme button
  is shared state too (`herdr-critters.theme`, a theme id; unknown or missing
  means `retro`).
- The mod sets the agent order (`setAgentOrder`) to the order it shows.

## Built from

- **Layout** `layouts/critters.json`: the shipped `main` layout with the
  `agents` block set to `{ "mod": "herdr-critters" }`, plus the pane collapse
  parts (see [Pane collapse](#pane-collapse)).
- **Mod** `mods/herdr-critters/`: `main.js` (one `View`, theme-agnostic),
  `mod.json` (`place: none`), `themes/` (registry `index.js` and one folder per
  theme with `theme.js` and `art/`), `fonts/`, `collapse.js` (see
  [Pane collapse](#pane-collapse)).
- **herdr functions**: `agents`, `terminals`, `spaces`, `machines`, `layout`,
  `theme`, `shared`, `setShared`, `setAgentOrder`, `run`, `openOverlay`,
  `closeOverlay`, `props`.
- **Commands**: `pane.focus`, `terminal.pin`, `terminal.peek`, and through
  `collapse.js`: `terminal.park`, `terminal.keep`, `tab.select`, `pane.swap`.
- **Shipped mods it uses**: the `pin`, `pin-off`, `plus`, `minus`,
  `chevron-down` and `chevron-right` icons of
  `workspace-chrome`.
- **Programs, network, files**: one program. To collapse a pane,
  `collapse.js` runs `hc connect` once to read the tab's split tree (read
  only). It does not reach the network or read files outside its own folder.
- **Art**: SVGs in `mods/herdr-critters/themes/<id>/art/`: one sprite
  per name and status (`sprite-<name>-<status>.svg`), a scene per status
  (`scene-<status>.svg`), a machine icon per scene (`icon-machine-<scene>.svg`)
  and `icon-dither.svg`. Made by
  `uv run --no-project art/generate.py --theme <id>` (default `retro`) from
  `art/themes/<id>/`: ASCII grids for retro (pixel art), drawing code for edo
  (vector woodblock prints), y2k (glossy vector critters) and cyber (neon
  vector mascots). A raster theme
  draws the same files as PNG (`.png` in place of `.svg`) and sets `artExt`:
  noir (black cutout critters, drawn with skia-python; run generate.py with
  `--with pillow --with skia-python`) and deepsea (soft gel critters, drawn with
  skia-python; also `--with imagequant`) and garden (felt craft critters, painted
  with Pillow and numpy; run generate.py with `--with numpy --with pillow`).
- **Fonts**: Silkscreen and VT323 (retro, noir, deepsea, garden), Shippori Mincho and Yuji Syuku cut
  to Latin letters (edo), Orbitron and Share Tech Mono (y2k, cyber), all SIL Open Font
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

## Extras

Extra tools that ship with the `critters` layout, beside the agents sidebar.

### Pane collapse

Hide a pane and keep its program running. Herdr has no command to shrink a
split, so a collapse parks the terminal (`terminal.park`): the pane goes away,
the program keeps running. A record of where the pane sat lets it come back.

**What you see**

- The terminal right-click menu has **Collapse pane** (a `minus` icon, the
  collapse key as its hint) just before **Close pane**. It shows only for a
  terminal pane in a tab with 2 or more panes, and acts on the pane that was
  right-clicked, not the focused one.
- Chips: a floating row at the bottom right of the `main` block, one chip per
  collapsed pane of the shown tab, plus any whose tab was closed. A chip is a
  26 px pill (radius 6, 1 px `border`, `raised` background, `hover` on
  hover) with the program icon, its name (max 160 px), the last folder of its
  cwd (`dim`, max 120 px) and its status: a spinner when working, a 6 px dot
  in `blocked` or `done`. A `minus` icon leads the row. No collapsed panes:
  the block draws nothing. The row goes vertical on a left or right edge.
- In the agents sidebar, a collapsed pane's agent stays in its group as a
  compact card (see below).

**How it behaves**

- Collapse (`collapse(target)` in `collapse.js`): find the pane; refuse a
  non-terminal pane or a tab's only pane with a warning toast. Read the tab's
  split tree from the machine's `herdr-app` document (`doc.get` over
  `hc connect`, read only). Walk up from the pane to the first split with 2 or
  more children. The neighbor is the sibling before it (or after it when it is
  first), and the anchor is that sibling's leaf on the side that touches the
  pane. Save `place` (`right` in a row, `down` in a column) and `swap`
  (`left` or `up` when the pane came first, else none). Then run
  `terminal.park`.
- The records are shared state `pane-collapse`: `{ items: [{ terminal,
  space, tab, name, icon, tint, cwd, at, anchor: { pane, terminal }, place,
  swap }] }`. Only records whose terminal is still live count.
- Expand (`expand(rec, cx)`): drop the record. If its tab is gone, run
  `terminal.keep` right of the focused pane (or as a new tab). Else
  `tab.select` the tab, `pane.focus` the anchor (else any pane of the tab, and
  no swap), `terminal.keep {place}`, wait (up to 2 s, 50 ms steps) for the new
  pane, then `pane.focus` it and `pane.swap` back.
- Keys (section `layout:critters` in `keys.json`): `cmd-shift-c` runs
  `pane-collapse.collapse` (the focused pane); `cmd-shift-e` runs
  `pane-collapse.expand` (the newest collapsed pane of the shown tab). The
  `pane-collapse` mod gets them through `nextCommand()`.
- A chip click runs `expand` for its record.
- Critters cards: a parked terminal leaves `agents()`. `herdr-critters` adds
  it back from the records and `terminals()` (only terminals with a status),
  after the last agent of its space, always as a compact card. A click on the
  card, or its plus button, runs `expand`. The card menu shows
  `EXPAND PANE` for it (and no card collapse), and `COLLAPSE PANE` for other
  cards.

**Built from**

- **Layout** `layouts/critters.json`: a floating block on `main`
  (`{ "id": "collapsed", "content": { "mod": "pane-collapse" }, "edge":
  "bottom", "align": "end" }`) and `"terminal_menu": "pane-collapse-menu"` on
  the root.
- **Mods** `mods/pane-collapse/` (`main.js`: the chips and the key commands;
  `mod.json` `place: none`) and `mods/pane-collapse-menu/` (a clone of the
  shipped `menu` from Herdr 0.1.12 with the `Collapse pane` item).
- **Shared code** `collapse.js`: the same file in `pane-collapse`,
  `pane-collapse-menu` and `herdr-critters`, because a mod can't import from
  another mod's folder. `install.sh` stops if the copies differ.
- **herdr functions**: `panes`, `spaces`, `focused`, `terminals`, `shared`,
  `setShared`, `notify`, `exec`, `run`, `nextCommand`, `keys`, `theme`,
  `placement`.
- **Commands**: `terminal.park`, `terminal.keep`, `tab.select`, `pane.focus`,
  `pane.swap`.
- **Programs**: `hc connect`, once per collapse, to read the split tree.

**Limits**

- Split sizes are not kept: the restored pane gets half of its neighbor.
- The place is exact only when the neighbor was a single pane; next to a
  group of panes, the pane comes back inside that group.
- A parked terminal has core keep off: if herdr-core restarts, it is lost.
- The menu is a copy; Herdr updates don't change it.
