"""The garden drawing kit: felt craft toys, drawn as raster art with Pillow and numpy.

Every shape is a felt piece: a fuzzy edge, a soft shadow on what is under it, puffy
matte shading (no shine) and fibers, often with a running stitch along its edge.
Faces are embroidered threads and buttons.

Shapes are given in design units and drawn at SS pixels per unit, then scaled down.
A sprite is 160 x 128 units, the feet on the bottom edge. Keep the top corners free:
top left x < 34, y < 44 (bolt, "!", check) and top right x > 130, y < 38 (sweat).

A shape ("prim") is a tuple:
  ("ellipse", cx, cy, rx, ry)   ("circle", cx, cy, r)   ("rect", x0, y0, x1, y1)
  ("poly", points)              ("line", points, width)
"""

import io
import math

import numpy as np
from PIL import Image, ImageDraw

SS = 4  # drawing pixels per design unit
W, H = 160, 128
STATUSES = ("idle", "working", "blocked", "done")

INK, LIGHT_INK = "#3a2a24", "#fbf3e2"  # face thread on a light body, on a dark body
PUPIL = "#2e2624"
MOUTH, BLUSH, RED_EYE = "#e8686a", "#f4a0a0", "#cc3b3b"
# Mark colors, matched to theme.js status colors.
GOLD, RED, BLUE, GREEN = "#e8a820", "#cc3b3b", "#5b96cc", "#3d8b37"
LIGHT = np.array([-0.45, -0.6, 0.66]) / np.linalg.norm([-0.45, -0.6, 0.66])  # from the top left


def rgb(h: str) -> np.ndarray:
    h = h.lstrip("#")
    return np.array([int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)], np.float32)


# ---- geometry (design units)


def qbez(p0, p1, p2, n=18):
    """Points on a quadratic curve from p0 to p2, pulled toward p1."""
    return [
        ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0], (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
        for t in np.linspace(0, 1, n)
    ]


def oval(cx, cy, rx, ry, deg=0.0, n=64, a0=0.0, a1=360.0):
    """Points around an ellipse turned by `deg`, from angle a0 to a1."""
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    pts = []
    for a in np.linspace(math.radians(a0), math.radians(a1), n):
        x, y = rx * math.cos(a), ry * math.sin(a)
        pts.append((cx + x * c - y * s, cy + x * s + y * c))
    return pts


def spiral(cx, cy, r0, r1, turns, start=0.0, n=160):
    return [
        (cx + (r0 + (r1 - r0) * t) * math.cos(start + t * turns * 2 * math.pi), cy + (r0 + (r1 - r0) * t) * math.sin(start + t * turns * 2 * math.pi))
        for t in np.linspace(0, 1, n)
    ]


def outline_of(prim):
    """A closed point loop around an ellipse, circle or polygon (None for other shapes)."""
    k = prim[0]
    if k == "ellipse":
        return oval(*prim[1:5])
    if k == "circle":
        return oval(prim[1], prim[2], prim[3], prim[3])
    if k == "poly":
        return list(prim[1]) + [prim[1][0]]
    return None


def inset(loop, by):
    """The loop pulled `by` units toward its middle."""
    cx = sum(p[0] for p in loop) / len(loop)
    cy = sum(p[1] for p in loop) / len(loop)
    out = []
    for x, y in loop:
        d = math.hypot(x - cx, y - cy) or 1
        f = max(0.0, 1 - by / d)
        out.append((cx + (x - cx) * f, cy + (y - cy) * f))
    return out


# ---- pixel arrays


def _draw(d, p, val):
    k = p[0]
    if k in ("ellipse", "circle"):
        cx, cy = p[1], p[2]
        rx, ry = (p[3], p[4]) if k == "ellipse" else (p[3], p[3])
        d.ellipse([(cx - rx) * SS, (cy - ry) * SS, (cx + rx) * SS, (cy + ry) * SS], fill=val)
    elif k == "rect":
        d.rectangle([p[1] * SS, p[2] * SS, p[3] * SS, p[4] * SS], fill=val)
    elif k == "poly":
        d.polygon([(x * SS, y * SS) for x, y in p[1]], fill=val)
    elif k == "line":
        _, pts, w = p
        d.line([(x * SS, y * SS) for x, y in pts], fill=val, width=max(1, round(w * SS)), joint="curve")
        for x, y in (pts[0], pts[-1]):  # round ends
            r = w * SS / 2
            d.ellipse([x * SS - r, y * SS - r, x * SS + r, y * SS + r], fill=val)
    else:
        raise ValueError(k)


def mask(w, h, prims) -> np.ndarray:
    """The shapes as a 0..1 coverage array, w x h units."""
    im = Image.new("L", (w * SS, h * SS), 0)
    d = ImageDraw.Draw(im)
    for p in prims:
        _draw(d, p, 255)
    return np.asarray(im, np.float32) / 255


_NOISE: dict = {}


def noise(shape, cell, seed, octaves=3) -> np.ndarray:
    """Smooth value noise in 0..1; `cell` is the first octave's feature size in pixels."""
    key = (shape, cell, seed, octaves)
    if key not in _NOISE:
        h, w = shape
        rng = np.random.default_rng(seed)
        out, amp, tot, c = np.zeros((h, w), np.float32), 1.0, 0.0, cell
        for _ in range(octaves):
            g = rng.random((max(2, int(h / c) + 2), max(2, int(w / c) + 2))).astype(np.float32)
            out += amp * np.asarray(Image.fromarray(g, "F").resize((w, h), Image.BICUBIC))
            tot += amp
            amp *= 0.5
            c /= 2
        out /= tot
        lo, hi = float(out.min()), float(out.max())
        _NOISE[key] = (out - lo) / (hi - lo + 1e-6)
    return _NOISE[key]


def _box(a, r, axis):
    if r < 1:
        return a
    pad = [(0, 0)] * a.ndim
    pad[axis] = (r + 1, r)
    c = np.cumsum(np.pad(a, pad, mode="edge"), axis=axis, dtype=np.float64)
    n = a.shape[axis]
    hi = np.take(c, np.arange(2 * r + 1, 2 * r + 1 + n), axis=axis)
    lo = np.take(c, np.arange(0, n), axis=axis)
    return ((hi - lo) / (2 * r + 1)).astype(np.float32)


def blur(a, radius_px) -> np.ndarray:
    """About a Gaussian blur: three box passes on each axis."""
    r = max(0, int(round(radius_px / 1.7)))
    for _ in range(3):
        a = _box(_box(a, r, 0), r, 1)
    return a


def warp(a, amp_px, cell_px, seed) -> np.ndarray:
    """Push each pixel around by smooth noise, up to `amp_px`."""
    h, w = a.shape
    dx = (noise((h, w), cell_px, seed) - 0.5) * 2 * amp_px
    dy = (noise((h, w), cell_px, seed + 101) - 0.5) * 2 * amp_px
    yy, xx = np.mgrid[0:h, 0:w]
    return a[np.clip(np.round(yy + dy), 0, h - 1).astype(int), np.clip(np.round(xx + dx), 0, w - 1).astype(int)]


def shift(a, dx_px, dy_px) -> np.ndarray:
    out = np.zeros_like(a)
    h, w = a.shape[:2]
    dx, dy = int(dx_px), int(dy_px)
    out[max(0, dy) : h + min(0, dy), max(0, dx) : w + min(0, dx)] = a[max(0, -dy) : h + min(0, -dy), max(0, -dx) : w + min(0, -dx)]
    return out


class Canvas:
    """A w x h unit picture, painted layer over layer (premultiplied color)."""

    def __init__(self, w, h, bg=None):
        self.w, self.h = w, h
        self.c = np.zeros((h * SS, w * SS, 3), np.float32)
        self.a = np.zeros((h * SS, w * SS), np.float32)
        if bg is not None:
            self.c[:] = bg
            self.a[:] = 1

    @property
    def shape(self):
        return self.a.shape

    def copy(self):
        out = Canvas(self.w, self.h)
        out.c, out.a = self.c.copy(), self.a.copy()
        return out

    def paint(self, color, alpha):
        """Paint `color` (a hex, an rgb triple or an array of them) over the canvas with `alpha`."""
        col = rgb(color) if isinstance(color, str) else np.asarray(color, np.float32)
        alpha = np.clip(alpha, 0, 1)
        self.c = self.c * (1 - alpha[..., None]) + col * alpha[..., None]
        self.a = self.a * (1 - alpha) + alpha

    def png(self, scale: float) -> bytes:
        """The picture as PNG bytes, `scale` pixels per unit, in at most 256 colors."""
        a = np.clip(self.a, 0, 1)
        c = np.where(a[..., None] > 1e-4, self.c / np.maximum(a[..., None], 1e-4), 0)
        arr = (np.dstack([np.clip(c, 0, 1), a]) * 255 + 0.5).astype(np.uint8)
        im = Image.fromarray(arr, "RGBA").resize((round(self.w * scale), round(self.h * scale)), Image.LANCZOS)
        im = im.quantize(256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        return buf.getvalue()


# ---- felt and thread


def felt(cv, m, color, seed, puff=5.0, drop=1.6, fuzz=1.0):
    """A felt piece in mask `m`: a fuzzy edge, a soft shadow below it, puffy matte shading."""
    m = blur(warp(m, 0.45 * SS * fuzz, 1.0 * SS, seed), 0.35 * SS)
    if drop:
        cv.paint("#3b2c1c", shift(blur(m, 2.2 * SS), 0.6 * drop * SS, drop * SS) * 0.3)
    gy, gx = np.gradient(blur(m, puff * SS))
    k = puff * SS * 1.5
    n = np.dstack([-gx * k, -gy * k, np.ones_like(gx)])
    n /= np.linalg.norm(n, axis=2, keepdims=True)
    shade = np.clip(0.3 + 0.95 * (n @ LIGHT), 0.6, 1.08)
    fib = noise(cv.shape, 0.5 * SS, seed % 7 + 3, octaves=2)
    mott = noise(cv.shape, 6 * SS, seed % 5 + 40, octaves=2)
    col = rgb(color) * (shade * (0.9 + 0.12 * fib + 0.05 * mott))[..., None]
    cv.paint(np.clip(col, 0, 1), m)


def dashes(pts, on=2.6, off=1.9):
    """Cut a polyline into short dashes: a running stitch."""
    out, cur, left, drawing = [], [pts[0]], on, True
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        seg = math.hypot(x1 - x0, y1 - y0)
        pos = 0.0
        while seg - pos > left:
            pos += left
            p = (x0 + (x1 - x0) * pos / seg, y0 + (y1 - y0) * pos / seg)
            if drawing:
                out.append(cur + [p])
            cur, drawing = [p], not drawing
            left = on if drawing else off
        left -= seg - pos
        cur.append((x1, y1))
    if drawing and len(cur) > 1:
        out.append(cur)
    return out


def stitch(cv, pts, color, width=1.0, on=2.6, off=1.9):
    """A running stitch along `pts` in thread `color` (a hex or an rgb triple)."""
    m = mask(cv.w, cv.h, [("line", d, width) for d in dashes(pts, on, off)])
    cv.paint("#2a2018", shift(blur(m, 0.4 * SS), 0.3 * SS, 0.5 * SS) * 0.35)
    cv.paint(color, m * 0.95)


def thread_of(color):
    """The stitch thread for a felt color: lighter, or darker on a pale felt."""
    c = rgb(color)
    return c * 0.7 if c.mean() > 0.78 else np.clip(c * 1.35 + 0.12, 0, 1)


def embroider(cv, m, color):
    """A raised thread line with a slanted twist (closed eyes, mouths)."""
    h, w = cv.shape
    yy, xx = np.mgrid[0:h, 0:w]
    twist = 0.85 + 0.15 * np.sin((xx + yy) * 2 * math.pi / (1.3 * SS))
    cv.paint("#2a2018", shift(blur(m, 0.5 * SS), 0, 0.5 * SS) * 0.3)
    cv.paint(np.clip(rgb(color) * twist[..., None], 0, 1), m)


# ---- critters


def piece(color, *prims, clip=None, puff=6.0, seam=True, patch=False):
    """A felt piece of a critter. `seam` sews a running stitch inside its edge; a `patch`
    is a small flat piece sewn on top (spots, stripes), clipped to `clip` shapes."""
    return {"color": color, "prims": list(prims), "clip": clip, "puff": 2.2 if patch else puff, "seam": seam and not patch,
            "drop": 0.9 if patch else 1.6, "cord": False}


def cord(color, pts, w):
    """A thin felt cord: legs, antennae, stems."""
    return {"color": color, "prims": [("line", pts, w)], "clip": None, "puff": 1.2, "seam": False, "drop": 1.0, "cord": True}


def pose(eyes, mouth, blush, r=4.6, light=False):
    """Where the face goes. `mouth` None leaves the mouth out (a beak); `light` stitches
    a light face for a dark body."""
    return {"eyes": eyes, "mouth": mouth, "blush": blush, "r": r, "light": light}


_BODIES: dict = {}


def body(name, parts) -> Canvas:
    """The critter without its face, drawn once and reused for every status."""
    if name not in _BODIES:
        cv = Canvas(W, H)
        for i, p in enumerate(parts):
            m = mask(W, H, p["prims"])
            if p["clip"]:
                m *= mask(W, H, p["clip"])
            felt(cv, m, p["color"], 10 + i * 3, puff=p["puff"], drop=p["drop"], fuzz=0.6 if p["cord"] else 1.0)
            if p["seam"]:
                for prim in p["prims"]:
                    loop = outline_of(prim)
                    if loop and (prim[0] != "circle" or prim[3] > 6):
                        stitch(cv, inset(loop, 3.2), thread_of(p["color"]))
        _BODIES[name] = cv
    return _BODIES[name].copy()


def face(cv, f, status):
    """Eyes, mouth and cheeks for a status: shut, open buttons, red buttons, happy arcs."""
    ink = LIGHT_INK if f["light"] else INK
    r, lw = f["r"], f["r"] * 0.5

    def thread(*prims, color=ink):
        embroider(cv, mask(W, H, list(prims)), color)

    def button(color, *prims, puff=2.0):
        felt(cv, mask(W, H, list(prims)), color, 200, puff=puff, drop=0.8, fuzz=0.3)

    if status != "idle":
        for bx, by in f["blush"]:
            felt(cv, mask(W, H, [("ellipse", bx, by, r * 1.3, r * 0.75)]), BLUSH, 210, puff=1.5, drop=0.5)
    for i, (x, y) in enumerate(f["eyes"]):
        if status == "idle":
            thread(("line", qbez((x - r, y), (x, y + r * 1.1), (x + r, y)), lw))
        elif status == "done":
            thread(("line", qbez((x - r, y + 1.5), (x, y - r * 1.5), (x + r, y + 1.5)), lw))
        elif status == "blocked":
            button(RED_EYE, ("circle", x, y, r * 1.05))
            cv.paint(PUPIL, blur(mask(W, H, [("circle", x, y, r * 0.42)]), 0.3 * SS))
            t = -1 if i == 0 else 1
            thread(("line", [(x - r, y - r - 3 + t * 2), (x + r, y - r - 3 - t * 2)], lw))
        else:
            button(ink, ("circle", x, y, r))
            dot = PUPIL if f["light"] else LIGHT_INK
            cv.paint(dot, blur(mask(W, H, [("circle", x + r * 0.35, y - r * 0.38, r * 0.36)]), 0.3 * SS))
    if f["mouth"] is None:
        return
    mx, my = f["mouth"]
    if status == "idle":
        thread(("line", [(mx - 3.5, my), (mx + 3.5, my)], lw))
    elif status == "working":
        thread(("line", qbez((mx - 5, my - 1), (mx, my + 4.5), (mx + 5, my - 1)), lw))
    elif status == "blocked":
        thread(("line", qbez((mx - 5, my + 2), (mx - 2.5, my - 2), (mx, my + 1)) + qbez((mx, my + 1), (mx + 2.5, my + 4), (mx + 5, my)), lw))
    else:
        d = [(mx - 6.5, my - 1.5)] + qbez((mx - 6.5, my - 1.5), (mx, my + 11), (mx + 6.5, my - 1.5))
        button(MOUTH, ("poly", d))
        thread(("line", d + [d[0]], lw * 0.8))


DROP = [(142, 6)] + qbez((142, 6), (133, 20), (135, 27)) + qbez((135, 27), (142, 37), (149, 27)) + qbez((149, 27), (151, 20), (142, 6))
BOLT = [(23, 3), (9, 23), (18, 23), (12, 40), (29, 16), (20, 16)]


def marks(cv, status):
    """Felt marks in the top corners: a bolt, a "!" and a sweat drop, a check."""

    def patch(color, prims, seam=None):
        felt(cv, mask(W, H, prims), color, 300, puff=2.5, drop=1.2, fuzz=0.6)
        if seam:
            stitch(cv, seam, thread_of(color), width=0.8, on=2, off=1.5)

    if status == "working":
        patch(GOLD, [("poly", BOLT)], inset(BOLT + BOLT[:1], 2.4))
    elif status == "blocked":
        patch(RED, [("line", [(16, 7), (16, 25)], 8), ("circle", 16, 35, 4.6)])
        patch(BLUE, [("poly", DROP)], inset(DROP, 2.4))
    elif status == "done":
        check = [(6, 22), (15, 32), (31, 9)]
        patch(GREEN, [("line", check, 7)], check)


def sprite(name, critter, status) -> bytes:
    """One critter's PNG for one status: the body, the face, the marks."""
    cv = body(name, critter["parts"])
    face(cv, critter["pose"], status)
    marks(cv, status)
    return cv.png(2)
