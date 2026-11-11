// Collapse a pane: park its terminal (the pane goes, the program keeps
// running) and remember where it was, so a chip can put it back.
// Shared state "pane-collapse" = { items: [record] }, one record per parked
// terminal: { terminal, space, tab, name, icon, tint, cwd, at,
//             anchor: { pane, terminal }, place, swap }.
// Restore: focus the anchor (the sibling it sat next to), terminal.keep
// beside it (place "right" or "down"), then pane.swap back when it sat
// before the anchor (swap "left" or "up").
// The same file lives in mods/pane-collapse, mods/pane-collapse-menu and
// mods/herdr-critters (a mod can't import from another mod's folder): keep
// the copies equal.

import { run, panes, spaces, focused, terminals, shared, setShared, notify, exec } from "herdr";

export const KEY = "pane-collapse";

export function collapsed() {
  return /** @type {any} */ (shared(KEY))?.items ?? [];
}

function save(items) {
  setShared(KEY, { items });
}

// Remote ids carry "<machine>/"; the core's own document doesn't.
function local(id) {
  const i = id ? id.indexOf("/") : -1;
  return i >= 0 ? id.slice(i + 1) : id;
}

// Live terminals only: a collapsed program that ended has nothing to restore.
export function live() {
  const alive = new Set(terminals().filter((t) => t.state === "live").map((t) => t.address));
  return collapsed().filter((r) => alive.has(r.terminal) || alive.has(local(r.terminal)));
}

function tabExists(tab) {
  return spaces().some((s) => s.tabs.some((t) => t.id === tab));
}

// The chips one tab shows: its own collapsed panes, plus any whose tab closed.
export function forTab(tab) {
  return live().filter((r) => r.tab === tab || !tabExists(r.tab));
}

// The tab's split tree from the machine's herdr-app document (read only).
async function tabTree(tab, machine) {
  const params = machine ? { name: "herdr-app", on: machine } : { name: "herdr-app" };
  const req = JSON.stringify({ jsonrpc: "2.0", id: 1, method: "doc.get", params });
  const r = await exec("sh", ["-c", 'printf "%s\\n" "$1" | hc connect', "sh", req]);
  for (const line of r.stdout.split("\n")) {
    let msg = null;
    try { msg = JSON.parse(line); } catch { continue; }
    if (msg?.id !== 1) continue;
    for (const s of msg.result?.value?.spaces ?? [])
      for (const t of s.tabs ?? []) if (t.id === local(tab)) return t.root;
  }
  return null;
}

// Path of nodes from the root to the block showing the terminal.
function pathTo(node, term) {
  if (!node) return null;
  if (node.type === "block") return node.content?.terminal === term ? [node] : null;
  for (const kid of node.children ?? []) {
    const p = pathTo(kid, term);
    if (p) return [node, ...p];
  }
  return null;
}

// The leaf of a sibling subtree that touches the collapsed pane's edge.
function edgeLeaf(node, horizontal, last) {
  while (node && node.type !== "block") {
    const kids = node.children ?? [];
    const along = (node.type === "row") === horizontal;
    node = along && last ? kids[kids.length - 1] : kids[0];
  }
  return node;
}

// Where the pane sits: the sibling to split from and how to get back.
function spot(root, term, machine) {
  const path = pathTo(root, local(term));
  if (!path) return null;
  for (let i = path.length - 2; i >= 0; i--) {
    const parent = path[i], kids = parent.children ?? [];
    if (kids.length < 2) continue;
    const at = kids.indexOf(path[i + 1]);
    const horizontal = parent.type === "row";
    const before = at > 0;
    const leaf = edgeLeaf(kids[before ? at - 1 : at + 1], horizontal, before);
    if (!leaf) return null;
    const prefix = machine ? `${machine}/` : "";
    return {
      anchor: { pane: prefix + leaf.id, terminal: leaf.content?.terminal ? prefix + leaf.content.terminal : null },
      place: horizontal ? "right" : "down",
      swap: before ? null : horizontal ? "left" : "up",
    };
  }
  return null;
}

function label(p) {
  return ((p.program?.agent || p.program?.shell) && p.program.name) || p.title || p.program?.name || "shell";
}

// target: { terminal, pane? }, from a menu's props().target or focused().
export async function collapse(target) {
  const p = panes().find((x) => (target.pane && x.pane === target.pane) || (target.terminal && x.terminal === target.terminal));
  if (!p?.terminal) {
    notify({ title: "Can't collapse this pane", body: "Only terminal panes collapse.", level: "warning" });
    return;
  }
  if (panes().filter((x) => x.tab === p.tab).length < 2) {
    notify({ title: "Can't collapse this pane", body: "It is the only pane in this tab.", level: "warning" });
    return;
  }
  const space = spaces().find((s) => s.tabs.some((t) => t.id === p.tab));
  let where = null;
  try { where = spot(await tabTree(p.tab, space?.machine), p.terminal, space?.machine); } catch (_e) { where = null; }
  const rec = {
    terminal: p.terminal,
    space: space?.id ?? null,
    tab: p.tab,
    name: label(p),
    icon: p.program?.icon ?? null,
    tint: Boolean(p.program?.tint),
    cwd: p.cwd,
    at: Date.now(),
    anchor: where?.anchor ?? null,
    place: where?.place ?? "right",
    swap: where?.swap ?? null,
  };
  save([...live().filter((r) => r.terminal !== p.terminal), rec]);
  run("terminal.park", { terminal: p.terminal });
}

// Puts a collapsed terminal back. cx: an async context, to wait for the
// new pane before swapping it to its old side.
export async function expand(rec, cx) {
  save(live().filter((r) => r.terminal !== rec.terminal));
  if (!tabExists(rec.tab)) {
    // Its tab closed: next to the focused pane, else as a new tab.
    run("terminal.keep", { terminal: rec.terminal, place: focused()?.pane ? "right" : "tab" });
    return;
  }
  run("tab.select", { id: rec.tab });
  const inTab = panes().filter((x) => x.tab === rec.tab);
  const a = rec.anchor;
  const anchor = (a?.terminal && inTab.find((x) => x.terminal === a.terminal)) || (a?.pane && inTab.find((x) => x.pane === a.pane));
  let swap = rec.swap;
  if (anchor) run("pane.focus", { pane: anchor.pane });
  else {
    // The sibling it sat by is gone: beside any pane of the tab.
    swap = null;
    const any = inTab.find((x) => x.focused) ?? inTab[0];
    if (any) run("pane.focus", { pane: any.pane });
  }
  run("terminal.keep", { terminal: rec.terminal, place: rec.place ?? "right" });
  if (!swap) return;
  // keep finishes in the background: wait for the pane, then swap it back.
  for (let i = 0; i < 40 && !panes().some((x) => x.terminal === rec.terminal); i++) await cx.sleep(50);
  if (!panes().some((x) => x.terminal === rec.terminal)) return;
  run("pane.focus", { terminal: rec.terminal });
  run("pane.swap", { direction: swap });
}

// The most recently collapsed chip a tab shows, for the expand key.
export function latest(tab) {
  const list = forTab(tab);
  return list.reduce((best, r) => (!best || r.at > best.at ? r : best), null);
}
