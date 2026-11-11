// Collapsed panes as chips, for a floating block over the tab:
//   "floating": [{ "id": "collapsed", "content": { "mod": "pane-collapse" }, "edge": "bottom", "align": "end" }]
// Shows the shown tab's collapsed panes (and any whose tab closed); click a
// chip to put the pane back. Renders nothing when there are none.
// Key commands (keys.json): "pane-collapse.collapse" collapses the focused
// pane, "pane-collapse.expand" puts back the last one collapsed in this tab.
// The terminal menu "pane-collapse-menu" collapses the right-clicked pane.

import { View, div, svg, image } from "gpui-kit";
import { h_flex, v_flex } from "gpui-base";
import { theme, focused, placement, terminals, nextCommand } from "herdr";
import { forTab, collapse, expand, latest } from "./collapse.js";

function icon(r, color) {
  if (!r.icon) return svg("mods/workspace-chrome/terminal.svg").size(13).flex_none().text_color(color);
  return r.tint ? svg(r.icon).size(13).flex_none().text_color(color) : image(r.icon).w(13).h(13).flex_none();
}

function base(cwd) {
  if (!cwd) return "";
  const parts = cwd.split("/").filter(Boolean);
  return parts[parts.length - 1] ?? "/";
}

export default class PaneCollapse extends View {
  init(_props, cx) {
    cx.spawn(async (cx) => {
      for (;;) {
        const c = await nextCommand();
        const f = focused();
        if (c === "collapse" && f?.pane && f.terminal) await collapse({ pane: f.pane, terminal: f.terminal });
        else if (c === "expand" && f?.tab) {
          const r = latest(f.tab);
          if (r) await expand(r, cx);
        }
        cx.notify();
      }
    });
  }

  render(cx) {
    const t = theme();
    const list = forTab(focused()?.tab);
    if (!list.length) return div();
    const status = new Map(terminals().map((x) => [x.address, x.status]));
    const stop = (_e, cx) => cx.stop_propagation();
    const chip = (r) => {
      const st = status.get(r.terminal);
      return h_flex()
        .id(`chip-${r.terminal}`)
        .h(26)
        .px(8)
        .gap(6)
        .flex_none()
        .items_center()
        .rounded(6)
        .border(1)
        .border_color(t.border)
        .bg(t.raised)
        .text_color(t.foreground)
        .hover((s) => s.bg(t.hover))
        .on_mouse_down("left", stop)
        .on_click((_e, cx) => {
          cx.stop_propagation();
          cx.spawn(async (cx) => { await expand(r, cx); });
        })
        .child(icon(r, t.muted))
        .child(div().max_w(160).truncate().child(r.name))
        .when(Boolean(r.cwd), (el) => el.child(div().max_w(120).truncate().text_color(t.dim).child(base(r.cwd))))
        .when(st === "working", (el) => el.child(svg("mods/workspace-chrome/spinner.svg").size(11).flex_none().text_color(t.working).spin(900)))
        .when(st === "blocked" || st === "done", (el) => el.child(div().size(6).flex_none().rounded(3).bg(t[st])));
    };
    const vertical = placement()?.vertical;
    return (vertical ? v_flex() : h_flex())
      .id("pane-collapse")
      .px(6)
      .gap(5)
      .items_center()
      .text_size(12)
      .child(svg("mods/workspace-chrome/minus.svg").size(13).flex_none().text_color(t.dim))
      .children(list.map(chip));
  }
}
