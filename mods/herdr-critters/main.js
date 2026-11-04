// Agents as retro cards: a pixel sprite in a scene, a status badge, the space and
// what it's doing. Grouped by machine; each machine has its own scene.

import { View, div, image, svg } from "gpui-kit";
import { v_flex, h_flex } from "gpui-base";
import { agents, terminals, spaces, machines, run, setAgentOrder, layout, shared, setShared, theme, openOverlay, closeOverlay, props } from "herdr";
import { webcrypto } from "crypto";
import { THEMES, themeById } from "./themes/index.js";

const THEME_KEY = "herdr-critters.theme";
const activeTheme = () => themeById(shared(THEME_KEY));

function find(node, id) {
  if (node?.id === id) return node;
  for (const child of node?.children ?? []) {
    const found = find(child, id);
    if (found) return found;
  }
  return null;
}

// The sidebar's rail goes by its width, as in the shipped agents mod.
const narrow = () => (find(layout(), "sidebar")?.size?.px ?? Infinity) < 160;

// An agent on another machine has a `machine/` address prefix.
const machineOf = (a) => (a.address.includes("/") ? a.address.split("/")[0] : null);

// A random item from the OS random source, so picks differ on every start.
const pickRandom = (arr) => arr[webcrypto.getRandomValues(new Uint32Array(1))[0] % arr.length];

const clean = (s) => (s ?? "").replace(/^[^\p{L}\p{N}]+/u, "").trim();

// The session's name: the terminal's core name, else the title the agent gives
// its terminal when that says more than the program's name or a folder.
function sessionName(a, terminal) {
  if (terminal?.name) return terminal.name;
  const live = clean(a.title);
  const generic = !live || live === a.program?.name || live.toLowerCase() === a.program?.key || /^[~/]|^[A-Za-z]:\\/.test(live) || live.includes("@");
  return generic ? null : live;
}

// The line under the name: "space -> session", else the space and its tab.
function detail(a, tabs, session) {
  if (session) return session;
  const tab = tabs.find((t) => t.id === a.tab);
  return tab?.named ? tab.name : tab ? `tab ${tab.name}` : a.program?.name ?? "";
}

// Cards go under their machine or under their space; the choice is shared state.
const GROUP_KEY = "herdr-critters.group";
const groupBy = () => (shared(GROUP_KEY) === "space" ? "space" : "machine");

// Collapsed groups ("space:<id>" / "machine:<name>") and compact cards (by address),
// each a shared map of id -> true.
const COLLAPSED_KEY = "herdr-critters.collapsed";
const COMPACT_KEY = "herdr-critters.compact";
const isSet = (key, id) => Boolean(shared(key)?.[id]);
function toggle(key, id) {
  const map = { ...(shared(key) ?? {}) };
  if (map[id]) delete map[id];
  else map[id] = true;
  setShared(key, map);
}

// The collapse id of the group an agent shows in.
const groupIdOf = (a) => (groupBy() === "space" ? `space:${a.space}` : `machine:${machineOf(a) ?? ""}`);

// Where a theme's picked names are stored. A theme can set `namesKey` to keep an old key
// (retro keeps "names" so current users keep their names).
const namesKey = (look) => look.namesKey ?? `names.${look.id}`;

// The art files' type: "svg" by default, "png" for a theme drawn as raster art.
const artExt = (look) => look.artExt ?? "svg";

export default class RetroAgents extends View {
  init() {
    this.hovered = null;
    this.look = null;
    this.picked = {};
  }

  // The status entry for an agent's word; an unknown word reads as idle.
  statusOf(s) {
    return this.look.status[s] ?? this.look.status.idle;
  }

  pixel(el, size, color) {
    return el.font_family(this.look.fonts.pixel).text_size(size).text_color(color);
  }

  // Switch to the active theme; each theme keeps its own picked names, kept across
  // restarts so a name doesn't change under you.
  useTheme(look) {
    if (this.look?.id === look.id) return;
    this.look = look;
    this.picked = JSON.parse(localStorage.getItem(namesKey(look)) ?? "{}");
  }

  // One name from the theme's names per agent, never two the same: an agent keeps its picked
  // name while no earlier agent holds it, else gets a random free one.
  names(list) {
    const out = new Map();
    const taken = new Set();
    const NAMES = this.look.names;
    let dirty = false;
    for (const a of list) {
      let name = this.picked[a.address];
      if (!name || !NAMES.includes(name) || taken.has(name)) {
        const free = NAMES.filter((n) => !taken.has(n));
        name = pickRandom(free.length ? free : NAMES);
        this.picked[a.address] = name;
        dirty = true;
      }
      // Only past 30 agents: the same name again, with a number.
      let unique = name;
      for (let n = 2; taken.has(unique); n++) unique = `${name} ${n}`;
      taken.add(unique);
      out.set(a.address, unique);
    }
    if (dirty) localStorage.setItem(namesKey(this.look), JSON.stringify(this.picked));
    return out;
  }

  // The sprite box: scene, sprite, and the corner badge that tells the state at a glance.
  // `name` is the agent's picked name: each name has its own sprite.
  stage(a, scene, w, h, name) {
    const { art, colors: C, status: STATUS } = this.look;
    const ext = artExt(this.look);
    const st = a.status;
    const spriteW = Math.round(w * 0.66);
    const spriteH = Math.round(spriteW * 0.8);
    const left = Math.round((w - spriteW) / 2);
    // Feet on the bricks: the scene's ground is its bottom 7 of 30 rows.
    const top = h - Math.round(h * (7 / 30)) - spriteH + 2;
    const sprite = image(`${art}/sprite-${name}-${STATUS[st] ? st : "idle"}.${ext}`).absolute().left(left).top(top).w(spriteW).h(spriteH);
    const badge = div()
      .absolute()
      .top(3)
      .right(3)
      .size(Math.max(12, Math.round(w * 0.2)))
      .flex()
      .items_center()
      .justify_center()
      .bg(C.badgeBg)
      .border(1)
      .border_color(st === "idle" ? C.idleEdge : this.statusOf(st).color);
    const mark = {
      idle: () => this.pixel(div(), 9, C.idleMark).frames(["z", "z", "Z", "Z"], 450),
      working: () => this.pixel(div(), 9, STATUS.working.color).frames(["▘", "▝", "▗", "▖"], 140),
      blocked: () => this.pixel(div(), 10, STATUS.blocked.color).child("!").loop("opacity", { from: 0.25, to: 1, period: 700 }),
      done: () => div().text_size(10).font_bold().text_color(STATUS.done.color).child("✓"),
    }[st] ?? (() => div());
    return div()
      .relative()
      .w(w)
      .h(h)
      .flex_none()
      .overflow_hidden()
      .border(2)
      .border_color(st === "idle" ? scene.box : this.statusOf(st).color + C.statusEdgeAlpha)
      .child(image(`${art}/scene-${STATUS[st] ? st : "idle"}.${ext}`).absolute().left(0).top(0).w(w - 4).h(h - 4))
      .child(st === "working" ? sprite.loop("top", { from: top, to: top - 3, period: 520 }) : sprite)
      .child(badge.child(mark()));
  }

  // A small icon button on a card; a click does `act` and not the card's own click.
  cardButton(id, tooltip, icon, act) {
    const C = this.look.colors;
    return div()
      .id(id)
      .flex_none()
      .p(2)
      .text_color(C.sub)
      .cursor_pointer()
      .hover((el) => el.text_color(C.text))
      .tooltip(tooltip)
      .on_click((_e, cx) => {
        cx.stop_propagation();
        act();
        this.hovered = null;
        cx.notify();
      })
      .child(svg(`mods/workspace-chrome/${icon}.svg`).size(12));
  }

  // The status word in its box.
  statusBox(a) {
    const s = this.statusOf(a.status);
    return this.pixel(div(), 10, s.color)
      .flex_none()
      .mt(-1)
      .px(5)
      .h(17)
      .flex()
      .items_center()
      .border(1)
      .border_color(a.status === "idle" ? this.look.colors.idleBox : s.color)
      .child(s.word);
  }

  // The card's frame: hover, click to focus, and the edge color.
  cardFrame(a, scene) {
    const { colors: C, status: STATUS } = this.look;
    const edge = a.focused ? C.focus : a.status === "blocked" ? STATUS.blocked.color : scene.edge;
    return h_flex()
      .id(`card-${a.address}`)
      .relative()
      .flex_none()
      .items_center()
      .bg(scene.card)
      .border(2)
      .border_color(edge)
      .cursor_pointer()
      .hover((el) => el.bg(scene.edge))
      .on_hover((on, cx) => {
        if (on) this.hovered = a.address;
        else if (this.hovered === a.address) this.hovered = null;
        cx.notify();
      })
      .on_click(() => run("pane.focus", { pane: a.pane }))
      .on_mouse_down("right", (_e, cx) => this.openMenu(a, cx));
  }

  // Right-click: a popup at the pointer, drawn by this mod with `props().menu`.
  openMenu(a, cx) {
    cx.stop_propagation();
    this.hovered = null;
    openOverlay({ mod: "herdr-critters", kind: "popup", frame: "none", width: 190, height: 92, props: { menu: a.address } });
  }

  // The context menu: pin, card collapse and group collapse for one agent.
  menu(address) {
    const { colors: C } = this.look;
    const a = agents().find((x) => x.address === address);
    const close = () => closeOverlay(props().overlay);
    if (!a) {
      close();
      return div();
    }
    const group = groupIdOf(a);
    const item = (id, label, act) => this.pixel(h_flex(), 10, C.sub)
      .id(`menu-${id}`)
      .h(26)
      .px(8)
      .items_center()
      .cursor_pointer()
      .hover((el) => el.bg(C.divider).text_color(C.text))
      .on_click(() => {
        act();
        close();
      })
      .child(label);
    return v_flex()
      .size_full()
      .p(4)
      .bg(C.bg)
      .border(2)
      .border_color(C.btnEdge)
      .child(item("pin", a.pinned ? "UNPIN" : "PIN TO TOP", () => run("terminal.pin", { terminal: a.address, pinned: !a.pinned })))
      .child(item("card", isSet(COMPACT_KEY, a.address) ? "EXPAND CARD" : "COLLAPSE CARD", () => toggle(COMPACT_KEY, a.address)))
      .child(item("group", isSet(COLLAPSED_KEY, group) ? "SHOW GROUP" : "COLLAPSE GROUP", () => toggle(COLLAPSED_KEY, group)));
  }

  pinButton(a) {
    return this.cardButton(`pin-${a.address}`, a.pinned ? "Unpin" : "Pin to the top", a.pinned ? "pin-off" : "pin",
      () => run("terminal.pin", { terminal: a.address, pinned: !a.pinned }));
  }

  compactButton(a, compact) {
    return this.cardButton(`compact-${a.address}`, compact ? "Expand the card" : "Collapse the card", compact ? "plus" : "minus",
      () => toggle(COMPACT_KEY, a.address));
  }

  // A collapsed card: one thin line with a small sprite, the name and the status.
  compactCard(a, scene, name) {
    const { colors: C, fonts } = this.look;
    const hot = this.hovered === a.address;
    return this.cardFrame(a, scene)
      .p(3)
      .gap(8)
      .child(this.stage(a, scene, 36, 30, this.picked[a.address]))
      .child(div().flex_1().min_w(0).font_family(fonts.mono).text_size(fonts.monoSize ?? 20).line_height(fonts.monoLine ?? "18px").text_color(C.text).truncate().child(name))
      .when(hot, (el) => el.child(this.compactButton(a, true)))
      .when(hot || a.pinned, (el) => el.child(this.pinButton(a)))
      .child(this.statusBox(a).mt(0).mr(2));
  }

  card(a, scene, tabs, name, session) {
    if (isSet(COMPACT_KEY, a.address)) return this.compactCard(a, scene, name);
    const { colors: C, fonts } = this.look;
    const hot = this.hovered === a.address;
    return this.cardFrame(a, scene)
      .p(6)
      .gap(10)
      .child(this.stage(a, scene, 74, 62, this.picked[a.address]))
      .child(
        v_flex()
          .flex_1()
          .min_w(0)
          .gap(5)
          .child(
            h_flex()
              .gap(6)
              .items_center()
              .child(div().flex_1().min_w(0).font_family(fonts.mono).text_size(fonts.monoSize ?? 20).line_height(fonts.monoLine ?? "18px").text_color(C.text).truncate().child(name))
              .child(this.statusBox(a)),
          )
          .child(div().text_size(11.5).text_color(C.sub).truncate().child(detail(a, tabs, session))),
      )
      .child(h_flex().absolute().bottom(4).right(4)
        .when(hot, (el) => el.child(this.compactButton(a, false)))
        .when(hot || a.pinned, (el) => el.child(this.pinButton(a))));
  }

  // A small outlined button in the top bar.
  headerButton(id, tooltip, onClick, label) {
    const C = this.look.colors;
    return this.pixel(div(), 9, C.sub)
      .id(id)
      .flex_none()
      .px(3)
      .h(15)
      .flex()
      .items_center()
      .border(1)
      .border_color(C.btnEdge)
      .cursor_pointer()
      .hover((el) => el.text_color(C.text).border_color(C.sub))
      .tooltip(tooltip)
      .on_click(onClick)
      .child(label);
  }

  // A group's header; a click collapses or opens the group.
  header(g, collapsed) {
    const { art, colors: C } = this.look;
    const ext = artExt(this.look);
    const busy = g.members.filter((a) => a.status === "working").length;
    return h_flex()
      .id(`group-${g.id}`)
      .flex_none()
      .h(30)
      .pt(6)
      .px(2)
      .gap(7)
      .items_center()
      .cursor_pointer()
      .tooltip(collapsed ? "Show the agents" : "Hide the agents")
      .on_click(() => toggle(COLLAPSED_KEY, g.id))
      .child(div().flex_none().text_color(C.sub).child(svg(`mods/workspace-chrome/${collapsed ? "chevron-right" : "chevron-down"}.svg`).size(12)))
      .child(image(`${art}/icon-machine-${g.scene.id}.${ext}`).w(15).h(11).flex_none())
      .child(this.pixel(div(), 11, g.color ?? C.machine).font_bold().truncate().child(g.label))
      .child(div().flex_1().min_w(8).h(2).bg(g.scene.edge))
      .child(this.pixel(div(), 11, g.scene.label).flex_none().child(`${busy}/${g.members.length}`));
  }

  // A small stage that focuses the agent's pane on a click.
  miniStage(a, scene) {
    const C = this.look.colors;
    return div()
      .id(`rail-${a.address}`)
      .flex_none()
      .border(2)
      .border_color(a.focused ? C.focus : C.clear)
      .cursor_pointer()
      .on_click(() => run("pane.focus", { pane: a.pane }))
      .on_mouse_down("right", (_e, cx) => this.openMenu(a, cx))
      .child(this.stage(a, scene, 36, 30, this.picked[a.address]));
  }

  // The rail: one small stage per agent.
  rail(list, sceneOf) {
    const C = this.look.colors;
    return v_flex()
      .size_full()
      .bg(C.bg)
      .items_center()
      .pt(8)
      .gap(6)
      .overflow_y_scrollbar()
      .children(list.map((a) => this.miniStage(a, sceneOf(a))));
  }

  render() {
    const look = activeTheme();
    this.useTheme(look);
    if (props()?.menu) return this.menu(props().menu);
    const { art, colors: C, status: STATUS } = look;
    const ext = artExt(look);
    const order = [null, ...machines().map((m) => m.name).filter((n) => n !== null)];
    const sceneOf = (a) => {
      const m = machineOf(a);
      const id = m === null ? look.localScene : look.remoteScenes[Math.max(0, order.indexOf(m) - 1) % look.remoteScenes.length];
      return { id, ...look.scenes[id] };
    };

    // agents() comes in machine, space order, so neighbours make a group either way.
    // Pins go first inside their group.
    const bySpace = groupBy() === "space";
    const t = theme();
    const spaceColors = shared("space.colors") ?? {};
    const groups = [];
    for (const a of agents()) {
      const m = machineOf(a);
      const key = bySpace ? a.space : m;
      if (groups.at(-1)?.key === key) {
        groups.at(-1).members.push(a);
        continue;
      }
      const scene = sceneOf(a);
      groups.push(bySpace
        ? { key, id: groupIdOf(a), label: (a.space_name || "space").toUpperCase(), color: t[spaceColors[a.space]], scene, members: [a] }
        : { key, id: groupIdOf(a), label: m === null ? "THIS MACHINE" : m.toUpperCase(), scene, members: [a] });
    }
    for (const g of groups) g.members = [...g.members.filter((a) => a.pinned), ...g.members.filter((a) => !a.pinned)];
    const list = groups.flatMap((g) => g.members);
    setAgentOrder(list.map((a) => a.address));

    const names = this.names(list);
    if (narrow()) return this.rail(list, sceneOf);

    const all = terminals();
    const tabs = spaces().flatMap((s) => s.tabs);
    const busy = list.filter((a) => a.status === "working").length;
    const byAddress = new Map(all.map((t) => [t.address, t]));

    // A collapsed group shows only its header.
    const rows = groups.flatMap((g) => {
      const collapsed = isSet(COLLAPSED_KEY, g.id);
      return [
        this.header(g, collapsed),
        ...(collapsed ? [] : g.members.map((a) => this.card(a, g.scene, tabs, names.get(a.address), sessionName(a, byAddress.get(a.address))))),
      ];
    });

    return v_flex()
      .size_full()
      .min_h(0)
      .bg(C.bg)
      .border_t(1)
      .border_color(C.divider)
      .child(
        h_flex()
          .flex_none()
          .h(38)
          .px(14)
          .pt(6)
          .items_center()
          .justify_between()
          .child(h_flex().flex_1().min_w(0).overflow_hidden().gap(5).items_center()
            .child(image(`${art}/icon-dither.${ext}`).size(12).flex_none())
            .child(this.pixel(div(), 11, C.head).flex_none().child("AGENTS"))
            .child(this.headerButton("critters-group", "Group agents by machine or by space", () => setShared(GROUP_KEY, bySpace ? "machine" : "space"), bySpace ? "BY SPACE" : "BY MACHINE"))
            .child(this.headerButton("critters-theme", "Switch the look of the cards", () => setShared(THEME_KEY, THEMES[(THEMES.indexOf(look) + 1) % THEMES.length].id), look.label)))
          .child(this.pixel(div(), 11, busy ? STATUS.working.color : C.head).flex_none().child(`${busy} ${STATUS.working.word}`)),
      )
      .when(list.length === 0, (el) =>
        el.child(v_flex().px(14).pt(10).gap(6)
          .child(this.pixel(div(), 11, C.machine).child("NO PLAYERS YET"))
          .child(div().text_size(11.5).text_color(C.sub).child("Agents show up here when they report their status."))))
      .child(v_flex().id("critters-list").flex_1().min_h(0).px(10).pb(10).gap(8).overflow_y_scrollbar().children(rows));
  }
}
