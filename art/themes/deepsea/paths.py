"""Path text for skia: a small parser for the SVG path commands the deepsea art uses.

skia-python cannot read SVG path text, so this turns absolute M L H V Q T C Z
commands into a skia.Path. Write every path with absolute commands only.
"""

import re

import skia

TOKEN = re.compile(r"[MLHVQTCZ]|-?\d*\.?\d+")
SIZE = {"M": 2, "L": 2, "H": 1, "V": 1, "Q": 4, "T": 2, "C": 6, "Z": 0}


def path(d: str) -> skia.Path:
    """Path text to a skia.Path. T mirrors the last Q control point, as in SVG."""
    p, toks, i = skia.Path(), TOKEN.findall(d), 0
    cur, start, ctrl, cmd = (0.0, 0.0), (0.0, 0.0), None, ""
    while i < len(toks):
        if toks[i].isalpha():
            cmd, i = toks[i], i + 1
        a = [float(t) for t in toks[i : i + SIZE[cmd]]]
        i += SIZE[cmd]
        if cmd == "M":
            p.moveTo(*a)
            cur = start = (a[0], a[1])
            ctrl, cmd = None, "L"  # more pairs after M are lines
            continue
        if cmd == "Z":
            p.close()
            cur, ctrl = start, None
            continue
        if cmd == "H":
            a = [a[0], cur[1]]
        elif cmd == "V":
            a = [cur[0], a[0]]
        if cmd == "T":
            c = (2 * cur[0] - ctrl[0], 2 * cur[1] - ctrl[1]) if ctrl else cur
            a = [c[0], c[1], *a]
        if len(a) == 4:
            p.quadTo(*a)
            ctrl = (a[0], a[1])
        elif len(a) == 6:
            p.cubicTo(*a)
            ctrl = None
        else:
            p.lineTo(*a)
            ctrl = None
        cur = (a[-2], a[-1])
    return p


def circle(cx: float, cy: float, r: float) -> skia.Path:
    p = skia.Path()
    p.addCircle(cx, cy, r)
    return p


def circle_d(cx: float, cy: float, r: float) -> str:
    """A circle as path text, for a Part."""
    k = r * 0.5523
    return (
        f"M{cx - r} {cy}C{cx - r} {cy - k} {cx - k} {cy - r} {cx} {cy - r}C{cx + k} {cy - r} {cx + r} {cy - k} {cx + r} {cy}"
        f"C{cx + r} {cy + k} {cx + k} {cy + r} {cx} {cy + r}C{cx - k} {cy + r} {cx - r} {cy + k} {cx - r} {cy}Z"
    )
