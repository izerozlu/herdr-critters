// Agents as retro cards: a pixel sprite in a scene, a status badge, the space and
// what it's doing. Grouped by machine; each machine has its own scene.

import { View, div, image, svg } from "gpui-kit";
import { v_flex, h_flex } from "gpui-base";
import { agents, terminals, spaces, machines, run, setAgentOrder, layout, shared, setShared, theme } from "herdr";
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

// Where a theme's picked names are stored. A theme can set `namesKey` to keep an old key
// (retro keeps "names" so current users keep their names).
const namesKey = (look) => look.namesKey ?? `names.${look.id}`;

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
    const st = a.status;
    const spriteW = Math.round(w * 0.66);
    const spriteH = Math.round(spriteW * 0.8);
    const left = Math.round((w - spriteW) / 2);
    // Feet on the bricks: the scene's ground is its bottom 7 of 30 rows.
    const top = h - Math.round(h * (7 / 30)) - spriteH + 2;
    const sprite = image(`${art}/sprite-${name}-${STATUS[st] ? st : "idle"}.svg`).absolute().left(left).top(top).w(spriteW).h(spriteH);
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
      .child(image(`${art}/scene-${STATUS[st] ? st : "idle"}.svg`).absolute().left(0).top(0).w(w - 4).h(h - 4))
      .child(st === "working" ? sprite.loop("top", { from: top, to: top - 3, period: 520 }) : sprite)
      .child(badge.child(mark()));
  }

  card(a, scene, tabs, name, session) {
    const { colors: C, status: STATUS, fonts } = this.look;
    const s = this.statusOf(a.status);
    const hot = this.hovered === a.address;
    const edge = a.focused ? C.focus : a.status === "blocked" ? STATUS.blocked.color : scene.edge;
    const pin = div()
      .id(`pin-${a.address}`)
      .absolute()
      .bottom(4)
      .right(4)
      .p(2)
      .text_color(C.sub)
      .cursor_pointer()
      .hover((el) => el.text_color(C.text))
      .tooltip(a.pinned ? "Unpin" : "Pin to the top")
      .on_click((_e, cx) => {
        cx.stop_propagation();
        run("terminal.pin", { terminal: a.address, pinned: !a.pinned });
        this.hovered = null;
        cx.notify();
      })
      .child(svg(`mods/workspace-chrome/${a.pinned ? "pin-off" : "pin"}.svg`).size(12));
    return h_flex()
      .id(`card-${a.address}`)
      .relative()
      .flex_none()
      .p(6)
      .gap(10)
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
              .child(
                this.pixel(div(), 10, s.color)
                  .flex_none()
                  .mt(-1)
                  .px(5)
                  .h(17)
                  .flex()
                  .items_center()
                  .border(1)
                  .border_color(a.status === "idle" ? C.idleBox : s.color)
                  .child(s.word),
              ),
          )
          .child(div().text_size(11.5).text_color(C.sub).truncate().child(detail(a, tabs, session))),
      )
      .when(hot || a.pinned, (el) => el.child(pin));
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

  header(g) {
    const { art, colors: C } = this.look;
    const busy = g.members.filter((a) => a.status === "working").length;
    return h_flex()
      .flex_none()
      .h(30)
      .pt(6)
      .px(2)
      .gap(7)
      .items_center()
      .child(image(`${art}/icon-machine-${g.scene.id}.svg`).w(15).h(11).flex_none())
      .child(this.pixel(div(), 11, g.color ?? C.machine).font_bold().truncate().child(g.label))
      .child(div().flex_1().min_w(8).h(2).bg(g.scene.edge))
      .child(this.pixel(div(), 11, g.scene.label).flex_none().child(`${busy}/${g.members.length}`));
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
      .children(list.map((a) => div()
        .id(`rail-${a.address}`)
        .border(2)
        .border_color(a.focused ? C.focus : C.clear)
        .cursor_pointer()
        .on_click(() => run("pane.focus", { pane: a.pane }))
        .child(this.stage(a, sceneOf(a), 36, 30, this.picked[a.address]))));
  }

  render() {
    const look = activeTheme();
    this.useTheme(look);
    const { art, colors: C, status: STATUS } = look;
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
        ? { key, label: (a.space_name || "space").toUpperCase(), color: t[spaceColors[a.space]], scene, members: [a] }
        : { key, label: m === null ? "THIS MACHINE" : m.toUpperCase(), scene, members: [a] });
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

    const rows = groups.flatMap((g) => [
      this.header(g),
      ...g.members.map((a) => this.card(a, g.scene, tabs, names.get(a.address), sessionName(a, byAddress.get(a.address)))),
    ]);

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
            .child(image(`${art}/icon-dither.svg`).size(12).flex_none())
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
