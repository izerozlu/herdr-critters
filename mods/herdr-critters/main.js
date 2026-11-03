// Agents as retro cards: a pixel sprite in a scene, a status badge, the space and
// what it's doing. Grouped by machine; each machine has its own scene.

import { View, div, image, svg } from "gpui-kit";
import { v_flex, h_flex } from "gpui-base";
import { agents, terminals, spaces, machines, run, setAgentOrder, layout, shared, setShared, theme } from "herdr";
import { webcrypto } from "crypto";

const ART = "mods/herdr-critters/art";
const PIXEL = "Silkscreen";
const MONO = "VT323";

// The retro palette is the point of this mod, so it doesn't follow the theme.
const C = {
  bg: "#12131b",
  head: "#6b6f82",
  machine: "#e8922e",
  focus: "#e8922e",
  text: "#f1ecff",
  sub: "#9a95b0",
};

// A scene per machine: this machine gets dusk, others take the rest in turn.
const SCENES = {
  dusk: { card: "#1f1830", edge: "#3e2f5c", box: "#4b3870", label: "#b49be0" },
  den: { card: "#181d26", edge: "#2a3442", box: "#34465a", label: "#8fb3c8" },
  dawn: { card: "#221819", edge: "#4a2e2a", box: "#6a3e30", label: "#e8b48c" },
  moss: { card: "#161e19", edge: "#2a3e2e", box: "#3a5a3a", label: "#a8d890" },
};
const REMOTE_SCENES = ["den", "dawn", "moss"];

const STATUS = {
  working: { word: "BUSY", color: "#5ee6f2" },
  blocked: { word: "HELP!", color: "#ff5a5a" },
  done: { word: "DONE", color: "#9be36a" },
  idle: { word: "IDLE", color: "#a9a3bf" },
};
const statusOf = (s) => STATUS[s] ?? STATUS.idle;

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

// Every agent's name, a character to follow: 4 to 7 letters each.
const NAMES = [
  "pixel", "byte", "nova", "rook", "ziggy", "mochi", "bolt", "echo", "juno", "kiwi",
  "luma", "miso", "nimbus", "onyx", "pepper", "quill", "rusty", "sprout", "tango", "umbra",
  "vega", "waffle", "yeti", "zephyr", "comet", "dusty", "fable", "gizmo", "hopper", "ivory",
];

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

// A sub-agent without a pane isn't in agents(): its raw word, error counting as blocked.
const kidStatus = (k, listed) => {
  const s = listed.get(k.address) ?? k.status;
  return s === "error" ? "blocked" : s === "done" ? "idle" : s;
};

const pixel = (el, size, color) => el.font_family(PIXEL).text_size(size).text_color(color);

export default class RetroAgents extends View {
  init() {
    this.hovered = null;
    // Each agent's picked name, kept across restarts so it doesn't change under you.
    this.picked = JSON.parse(localStorage.getItem("names") ?? "{}");
  }

  // One name from NAMES per agent, never two the same: an agent keeps its picked
  // name while no earlier agent holds it, else gets a random free one.
  names(list) {
    const out = new Map();
    const taken = new Set();
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
    if (dirty) localStorage.setItem("names", JSON.stringify(this.picked));
    return out;
  }

  // The sprite box: scene, sprite, and the corner badge that tells the state at a glance.
  // `name` is the agent's NAMES name: each name has its own sprite.
  stage(a, scene, w, h, name) {
    const st = a.status;
    const spriteW = Math.round(w * 0.66);
    const spriteH = Math.round(spriteW * 0.8);
    const left = Math.round((w - spriteW) / 2);
    // Feet on the bricks: the scene's ground is its bottom 7 of 30 rows.
    const top = h - Math.round(h * (7 / 30)) - spriteH + 2;
    const sprite = image(`${ART}/sprite-${name}-${STATUS[st] ? st : "idle"}.svg`).absolute().left(left).top(top).w(spriteW).h(spriteH);
    const badge = div()
      .absolute()
      .top(3)
      .right(3)
      .size(Math.max(12, Math.round(w * 0.2)))
      .flex()
      .items_center()
      .justify_center()
      .bg("#0b0b12cc")
      .border(1)
      .border_color(st === "idle" ? "#8a849e" : statusOf(st).color);
    const mark = {
      idle: () => pixel(div(), 9, "#d8d2ee").frames(["z", "z", "Z", "Z"], 450),
      working: () => pixel(div(), 9, STATUS.working.color).frames(["▘", "▝", "▗", "▖"], 140),
      blocked: () => pixel(div(), 10, STATUS.blocked.color).child("!").loop("opacity", { from: 0.25, to: 1, period: 700 }),
      done: () => div().text_size(10).font_bold().text_color(STATUS.done.color).child("✓"),
    }[st] ?? (() => div());
    return div()
      .relative()
      .w(w)
      .h(h)
      .flex_none()
      .overflow_hidden()
      .border(2)
      .border_color(st === "idle" ? scene.box : statusOf(st).color + "99")
      .child(image(`${ART}/scene-${STATUS[st] ? st : "idle"}.svg`).absolute().left(0).top(0).w(w - 4).h(h - 4))
      .child(st === "working" ? sprite.loop("top", { from: top, to: top - 3, period: 520 }) : sprite)
      .child(badge.child(mark()));
  }

  card(a, scene, tabs, name, session) {
    const s = statusOf(a.status);
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
              .child(div().flex_1().min_w(0).font_family(MONO).text_size(20).line_height("18px").text_color(C.text).truncate().child(name))
              .child(
                pixel(div(), 10, s.color)
                  .flex_none()
                  .mt(-1)
                  .px(5)
                  .h(17)
                  .flex()
                  .items_center()
                  .border(1)
                  .border_color(a.status === "idle" ? "#6a6380" : s.color)
                  .child(s.word),
              ),
          )
          .child(div().text_size(11.5).text_color(C.sub).truncate().child(detail(a, tabs, session))),
      )
      .when(hot || a.pinned, (el) => el.child(pin));
  }

  // Live sub-agents of `addr`, depth first.
  kids(all, addr, depth = 0) {
    return all
      .filter((k) => k.parent === addr && k.state === "live")
      .flatMap((k) => [{ t: k, depth }, ...this.kids(all, k.address, depth + 1)]);
  }

  kidRow(k, depth, listed) {
    const s = statusOf(kidStatus(k, listed));
    return h_flex()
      .id(`sub-${k.address}`)
      .flex_none()
      .h(22)
      .pl(14 + depth * 10)
      .pr(8)
      .gap(6)
      .items_center()
      .cursor_pointer()
      .hover((el) => el.bg("#ffffff0d"))
      .on_click(() => run("terminal.peek", { terminal: k.address }))
      .child(pixel(div(), 10, C.head).child("└"))
      .child(div().flex_1().min_w(0).truncate().text_size(11.5).text_color(C.sub).child(k.name || k.template || k.program?.name || k.address))
      .child(pixel(div(), 8, s.color).child(s.word));
  }

  header(g) {
    const busy = g.members.filter((a) => a.status === "working").length;
    return h_flex()
      .flex_none()
      .h(30)
      .pt(6)
      .px(2)
      .gap(7)
      .items_center()
      .child(image(`${ART}/icon-machine-${g.scene.id}.svg`).w(15).h(11).flex_none())
      .child(pixel(div(), 11, g.color ?? C.machine).font_bold().truncate().child(g.label))
      .child(div().flex_1().min_w(8).h(2).bg(g.scene.edge))
      .child(pixel(div(), 11, g.scene.label).flex_none().child(`${busy}/${g.members.length}`));
  }

  // The rail: one small stage per agent.
  rail(list, sceneOf) {
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
        .border_color(a.focused ? C.focus : "#00000000")
        .cursor_pointer()
        .on_click(() => run("pane.focus", { pane: a.pane }))
        .child(this.stage(a, sceneOf(a), 36, 30, this.picked[a.address]))));
  }

  render() {
    const order = [null, ...machines().map((m) => m.name).filter((n) => n !== null)];
    const sceneOf = (a) => {
      const m = machineOf(a);
      const id = m === null ? "dusk" : REMOTE_SCENES[Math.max(0, order.indexOf(m) - 1) % REMOTE_SCENES.length];
      return { id, ...SCENES[id] };
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
    const listed = new Map(list.map((a) => [a.address, a.status]));
    const tabs = spaces().flatMap((s) => s.tabs);
    const busy = list.filter((a) => a.status === "working").length;
    const byAddress = new Map(all.map((t) => [t.address, t]));

    const rows = groups.flatMap((g) => [
      this.header(g),
      ...g.members.flatMap((a) => [
        this.card(a, g.scene, tabs, names.get(a.address), sessionName(a, byAddress.get(a.address))),
        ...this.kids(all, a.address).map((k) => this.kidRow(k.t, k.depth, listed)),
      ]),
    ]);

    return v_flex()
      .size_full()
      .min_h(0)
      .bg(C.bg)
      .border_t(1)
      .border_color("#22232e")
      .child(
        h_flex()
          .flex_none()
          .h(38)
          .px(14)
          .pt(6)
          .items_center()
          .justify_between()
          .child(h_flex().gap(8).items_center()
            .child(image(`${ART}/icon-dither.svg`).size(12).flex_none())
            .child(pixel(div(), 11, C.head).child("AGENTS"))
            .child(
              pixel(div(), 9, C.sub)
                .id("critters-group")
                .px(4)
                .h(15)
                .flex()
                .items_center()
                .border(1)
                .border_color("#34364a")
                .cursor_pointer()
                .hover((el) => el.text_color(C.text).border_color(C.sub))
                .tooltip("Group agents by machine or by space")
                .on_click(() => setShared(GROUP_KEY, bySpace ? "machine" : "space"))
                .child(bySpace ? "BY SPACE" : "BY MACHINE"),
            ))
          .child(pixel(div(), 11, busy ? STATUS.working.color : C.head).child(`${busy} BUSY`)),
      )
      .when(list.length === 0, (el) =>
        el.child(v_flex().px(14).pt(10).gap(6)
          .child(pixel(div(), 11, C.machine).child("NO PLAYERS YET"))
          .child(div().text_size(11.5).text_color(C.sub).child("Agents show up here when they report their status."))))
      .child(v_flex().id("critters-list").flex_1().min_h(0).px(10).pb(10).gap(8).overflow_y_scrollbar().children(rows));
  }
}
