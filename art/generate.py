"""Generate the herdr-critters pixel art (sprites, scenes, icons) as SVG.

Each picture is an ASCII grid: one character per pixel, "." is transparent.
Run from the repo root:  uv run art/generate.py
"""

import importlib
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "mods" / "herdr-critters" / "art"

# ---- sprites: 20 x 16, drawn standing on the scene's ground. Each is keyed by the
# agent name it belongs to (mods/herdr-critters/main.js NAMES); more are in sprites/.

SPRITES: dict[str, tuple[dict[str, str], list[str]]] = {
    "byte": (
        {"r": "#e0483e", "G": "#5b6472", "L": "#c9d1dc", "c": "#5ee6f2", "d": "#3a404a", "D": "#2b3038", "b": "#e0483e"},
        [
            ".........r..........",
            ".........G..........",
            ".....GGGGGGGGGG.....",
            "....GLLLLLLLLLLG....",
            "....GLccLLLLccLG....",
            "....GLccLLLLccLG....",
            "....GLLLLLLLLLLG....",
            "....GLLLddddLLLG....",
            "....GGGGGGGGGGGG....",
            "......DDDDDDDD......",
            ".....GLLLLLLLLG.....",
            "...GGGLbLLLLcLGGG...",
            "...G.GLLLLLLLLG.G...",
            ".....GGGGGGGGGG.....",
            "......DD....DD......",
            ".....DDD....DDD.....",
        ],
    ),
    "pixel": (
        {"B": "#e8d9b0", "b": "#b8a67c", "S": "#1b2a3a", "c": "#5ee6f2", "r": "#e0483e", "D": "#6e6250"},
        [
            "....................",
            "...BBBBBBBBBBBBBB...",
            "...BSSSSSSSSSSSSB...",
            "...BSSSSSSSSSSSSB...",
            "...BSSScSSSScSSSB...",
            "...BSSScSSSScSSSB...",
            "...BSSSSSSSSSSSSB...",
            "...BSScSSSSSSScSB...",
            "...BSSSccccccSSSB...",
            "...BSSSSSSSSSSSSB...",
            "...BBBBBBBBBBBBBB...",
            "...BrbBBBBBBBBbbB...",
            "...bbbbbbbbbbbbbb...",
            ".......DDDDDD.......",
            ".....bbbbbbbbbb.....",
            ".....DDDDDDDDDD.....",
        ],
    ),
    "quill": (
        {"Y": "#f7c83a", "y": "#d89a1c", "H": "#7a5a2c", "h": "#a07a3c", "k": "#1a1a1a", "o": "#f08a24", "w": "#fff4c8"},
        [
            "......HHHHH.........",
            ".....HhhhhhH........",
            "....HhhhhhhhH.......",
            "....HYYYYYYYH.......",
            "....YYwkYYYYY.......",
            "....YYkkYYYYYoo.....",
            "....YYYYYYYYYooo....",
            ".....YYYYYYYY.......",
            "......YYYY..........",
            "...YYYYYYYYYYY......",
            "..YYYYYYYYYYYYY..Y..",
            "..YYYyyyyyYYYYYYYY..",
            "..YYYYyyyyYYYYYYY...",
            "...YYYYYYYYYYYYY....",
            ".....oo....oo.......",
            "....ooo...ooo.......",
        ],
    ),
    "miso": (
        {"K": "#d9944a", "k": "#f4dcb0", "s": "#8a4e22", "g": "#2f7a2a", "p": "#f29bb6", "w": "#fff0d8"},
        [
            "....................",
            "....K........K......",
            "....KK......KK......",
            "....KpK....KpK......",
            "....KKKsKKsKKK......",
            "...KKKKsKKsKKKK.....",
            "...KKgKKKKKKgKK.....",
            "...KKgKKKKKKgKK.....",
            "...wKKKKppKKKKw.....",
            "....KKKKKKKKKK......",
            "....KsKKKKKKKsK..s..",
            "...KKKkkkkkkKKK..K..",
            "...KKKkkkkkkKKKKsK..",
            "...KKKKKKKKKKKKKK...",
            "...KK.KK..KK.KK.....",
            "...ww.ww..ww.ww.....",
        ],
    ),
    "umbra": (
        {"W": "#e9e6ff", "w": "#b9b2e8", "k": "#2a2440", "p": "#f29bb6"},
        [
            "....................",
            "......WWWWWWW.......",
            ".....WWWWWWWWW......",
            "....WWWWWWWWWWW.....",
            "....WWkkWWWkkWW.....",
            "....WWkkWWWkkWW.....",
            "....WpWWWWWWWpW.....",
            "....WWWWkkkWWWW.....",
            "....WWWWWWWWWWW.....",
            "....WWWWWWWWWWW.....",
            "....WwWWWWWWWwW.....",
            "....WwwWWWWWwwW.....",
            "....WWWWWWWWWWW.....",
            "....WWW.WWW.WWW.....",
            "....WW...W...WW.....",
            "....................",
        ],
    ),
}

# ---- poses: each sprite gets one picture per agent status

STATUSES = ("idle", "working", "blocked", "done")

# Colors every pose may use on top of a sprite's own palette.
POSE_COLORS = {"R": "#ff5a5a", "X": "#ff5a5a", "q": "#6ec8ff", "E": "#9be36a", "U": "#fff27a"}

# Small marks placed in free space beside the sprite.
BANG = ["X", "X", "X", ".", "X"]
SWEAT = ["q", "q"]
CHECK = ["...E", "E.E.", ".E.."]
BOLT = [".U", "UU", "U."]

# Per sprite: the face color, the color of a closed eye, the top pixel of each
# eye (the eye is that pixel and the one under it), and extra pixels per status
# as (x, y, text) where text overwrites from x.
POSES: dict[str, dict] = {
    "byte": {
        "face": "L", "line": "d", "eyes": [(6, 4), (7, 4), (12, 4), (13, 4)],
        "idle": [(9, 0, "d")],
        "working": [(9, 0, "U"), (7, 11, "U"), (12, 11, "E")],
        "blocked": [(7, 7, "dLdLd")],
        "done": [(7, 6, "d"), (12, 6, "d")],
    },
    "pixel": {
        "face": "S", "line": "c", "eyes": [(7, 4), (12, 4)],
        "idle": [(6, 7, "S"), (13, 7, "S"), (7, 8, "S"), (12, 8, "S"), (4, 11, "D")],
        "working": [(4, 11, "E")],
        "blocked": [(6, 7, "S"), (13, 7, "S"), (6, 9, "c"), (13, 9, "c")],
        "done": [],
    },
    "quill": {
        "face": "Y", "line": "k", "eyes": [(6, 4), (7, 4)],
        "idle": [],
        "working": [(8, 1, "U")],
        "blocked": [],
        "done": [],
    },
    "miso": {
        "face": "K", "line": "s", "eyes": [(5, 6), (12, 6)],
        "idle": [(5, 3, "s"), (12, 3, "s")],
        "working": [(5, 3, "U"), (12, 3, "U")],
        "blocked": [(8, 8, "ss"), (8, 9, "ss")],
        "done": [(4, 8, "p"), (13, 8, "p"), (7, 9, "sKKs")],
    },
    "umbra": {
        "face": "W", "line": "k", "eyes": [(6, 4), (7, 4), (11, 4), (12, 4)],
        "idle": [(8, 7, "WkW")],
        "working": [],
        "blocked": [(8, 8, "kkk")],
        "done": [(7, 7, "kWWWk"), (8, 8, "kkk")],
    },
}


# Sprite batches in sprites/*.py, each with its own SPRITES and POSES.
for _path in sorted((Path(__file__).resolve().parent / "sprites").glob("*.py")):
    if _path.stem.startswith("_"):
        continue
    # One batch at a time: others may be half drawn.
    if "--batch" in sys.argv and _path.stem != sys.argv[sys.argv.index("--batch") + 1]:
        continue
    _batch = importlib.import_module(f"sprites.{_path.stem}")
    assert not set(_batch.SPRITES) & set(SPRITES), f"{_path.name}: sprite name taken"
    assert set(_batch.SPRITES) == set(_batch.POSES), f"{_path.name}: SPRITES and POSES differ"
    SPRITES.update(_batch.SPRITES)
    POSES.update(_batch.POSES)


def put(rows: list[str], x: int, y: int, text: str) -> None:
    rows[y] = rows[y][:x] + text + rows[y][x + len(text) :]


def place(rows: list[str], glyph: list[str], side: str) -> None:
    """Put a glyph in the highest free spot: on `side` one pixel clear of the sprite,
    else on the other side, else touching it."""
    for s, margin in ((side, 1), ("left" if side == "right" else "right", 1), (side, 0)):
        if place_at(rows, glyph, s, margin):
            return


def place_at(rows: list[str], glyph: list[str], side: str, margin: int) -> bool:
    h, w = len(rows), len(rows[0])
    gh, gw = len(glyph), len(glyph[0])
    xs = range(w - gw, -1, -1) if side == "right" else range(0, w - gw + 1)

    def free(x: int, y: int) -> bool:
        for gy, line in enumerate(glyph):
            for gx, ch in enumerate(line):
                if ch == ".":
                    continue
                for ny in range(y + gy - margin, y + gy + margin + 1):
                    for nx in range(x + gx - margin, x + gx + margin + 1):
                        if 0 <= ny < h and 0 <= nx < w and rows[ny][nx] != ".":
                            return False
        return True

    for y in range(0, h - gh + 1):
        for x in xs:
            if free(x, y):
                for gy, line in enumerate(glyph):
                    for gx, ch in enumerate(line):
                        if ch != ".":
                            put(rows, x + gx, y + gy, ch)
                return True
    return False


def pose(name: str, status: str) -> tuple[dict[str, str], list[str]]:
    palette, base = SPRITES[name]
    p = POSES[name]
    rows = list(base)
    for x, y in p["eyes"]:
        if status == "idle":  # closed: a line where the eye's bottom was
            put(rows, x, y, p["face"])
            put(rows, x, y + 1, p["line"])
        elif status == "blocked":
            put(rows, x, y, "R")
            put(rows, x, y + 1, "R")
        elif status == "done":  # happy: only the top half, an upturned eye
            put(rows, x, y + 1, p["face"])
    for x, y, text in p[status]:
        put(rows, x, y, text)
    if status == "working":
        place(rows, BOLT, "left")
    elif status == "blocked":
        place(rows, BANG, "left")
        place(rows, SWEAT, "right")
    elif status == "done":
        place(rows, CHECK, "left")
    return {**palette, **POSE_COLORS}, rows


# ---- scenes: 36 x 30, the sprite box behind each agent; one per machine

SCENE_W, SCENE_H, GROUND = 36, 30, 7


def scene(sky: list[str], star: str, brick: str, mortar: str, glow: str) -> tuple[dict[str, str], list[str]]:
    """Sky bands on top, a star, a horizon glow line, then bricks."""
    pal = {"a": sky[0], "b": sky[1], "c": sky[2], "s": star, "B": brick, "m": mortar, "g": glow}
    rows: list[str] = []
    sky_rows = SCENE_H - GROUND
    for y in range(sky_rows):
        band = "a" if y < sky_rows * 0.45 else "b" if y < sky_rows * 0.8 else "c"
        rows.append(band * SCENE_W)
    # A star with a twinkle cross, top left.
    for x, y in ((3, 2), (2, 3), (3, 3), (4, 3), (3, 4)):
        rows[y] = rows[y][:x] + "s" + rows[y][x + 1 :]
    for x, y in ((28, 5), (17, 2)):
        rows[y] = rows[y][:x] + "s" + rows[y][x + 1 :]
    rows[-1] = "g" * SCENE_W
    for y in range(GROUND):
        if y % 3 == 2:
            rows.append("m" * SCENE_W)
            continue
        offset = 0 if (y // 3) % 2 == 0 else 3
        rows.append("".join("m" if (x + offset) % 6 == 0 else "B" for x in range(SCENE_W)))
    return pal, rows


SCENES = {
    "dusk": scene(["#1e1830", "#2a1f42", "#3a2554"], "#ffd27a", "#4a2440", "#2e1628", "#c0467a"),
    "den": scene(["#141b24", "#18222e", "#1d2b38"], "#9fe8ff", "#24525a", "#163238", "#3fa7a7"),
    "dawn": scene(["#2a1a22", "#40222a", "#5a2e2c"], "#ffe6a0", "#5a3a22", "#3a2414", "#f08a24"),
    "moss": scene(["#141e18", "#18281e", "#1e3424"], "#d8ff9a", "#2e4a26", "#1c2e18", "#7ac25a"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Dark enough that every sprite still reads.
    "idle": scene(["#15151d", "#1b1b26", "#222231"], "#8a86a0", "#2c2a3a", "#1c1b26", "#5a5670"),
    "working": scene(["#0c1f28", "#10303c", "#154452"], "#9fe8ff", "#1d4c58", "#103038", "#5ee6f2"),
    "blocked": scene(["#220c12", "#36111a", "#4c1622"], "#ffb0a0", "#4a1a22", "#2c0e14", "#ff5a5a"),
    "done": scene(["#0e1f14", "#14301c", "#1a4226"], "#d8ff9a", "#24502c", "#14301a", "#9be36a"),
}

# ---- icons

ICONS = {
    # The header's dither block.
    "dither": ({"x": "#5a5f70"}, ["x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x"]),
    # A machine: monitor on a stand. Colored per machine by the scene's glow.
    **{
        f"machine-{name}": (
            {"F": pal["g"], "S": pal["a"], "s": pal["s"], "D": pal["m"]},
            ["FFFFFFFFFF", "FSSSSSSSSF", "FSsSSSSSSF", "FSSSSSSSSF", "FFFFFFFFFF", "...DDDD...", ".DDDDDDDD."],
        )
        for name, (pal, _rows) in SCENES.items()
    },
}


def svg(palette: dict[str, str], rows: list[str]) -> str:
    w, h = len(rows[0]), len(rows)
    assert all(len(r) == w for r in rows), "ragged grid"
    rects: list[str] = []
    for y, row in enumerate(rows):
        x = 0
        while x < w:
            ch = row[x]
            if ch == ".":
                x += 1
                continue
            run = x
            while run < w and row[run] == ch:
                run += 1
            rects.append(f'<rect x="{x}" y="{y}" width="{run - x}" height="1" fill="{palette[ch]}"/>')
            x = run
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w * 8}" height="{h * 8}" '
        f'shape-rendering="crispEdges">{"".join(rects)}</svg>\n'
    )


def main() -> None:
    # `--batch <name> <dir>`: only that batch's sprites, into <dir>, for drawing one
    # batch without touching the mod's art.
    args = sys.argv[1:]
    names, out = list(SPRITES), OUT
    if args[:1] == ["--batch"]:
        names = list(importlib.import_module(f"sprites.{args[1]}").SPRITES)
        out = Path(args[2])
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("sprite-*.svg"):
        old.unlink()
    poses = {f"{name}-{status}": pose(name, status) for name in names for status in STATUSES}
    for group, items in (("sprite", poses), ("scene", SCENES), ("icon", ICONS)):
        for name, (palette, rows) in items.items():
            (out / f"{group}-{name}.svg").write_text(svg(palette, rows))
    print(f"wrote {len(poses) + len(SCENES) + len(ICONS)} files to {out}")


if __name__ == "__main__":
    main()
