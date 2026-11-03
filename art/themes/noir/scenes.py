"""Noir scenes (the sprite box behind each agent, one per machine and per status) and icons."""

# 36 x 30 grids.
SCENE_W, SCENE_H, GROUND = 36, 30, 7

# The skyline: (left, right, top row) per building, and the rain streaks (x, top row).
BUILDINGS = [(0, 5, 12), (5, 9, 16), (9, 15, 10), (15, 20, 14), (20, 27, 8), (27, 31, 13), (31, 36, 11)]
RAIN = [(4, 5), (11, 2), (19, 8), (27, 3), (33, 12), (8, 14), (23, 16), (15, 0), (30, 18), (2, 17)]


def scene(sky: list[str], moon: str, block: str, window: str, rain: str, stone: str, gap: str, glow: str) -> tuple[dict[str, str], list[str]]:
    """Sky bands on top, a moon, a skyline with lit windows, rain, a glow line, then wet cobbles."""
    pal = {"a": sky[0], "b": sky[1], "c": sky[2], "s": moon, "K": block, "w": window, "r": rain,
           "P": stone, "m": gap, "g": glow}
    sky_rows = SCENE_H - GROUND
    rows = [list(("a" if y < sky_rows * 0.45 else "b" if y < sky_rows * 0.8 else "c") * SCENE_W) for y in range(sky_rows)]
    # A small moon, top left.
    for x, y in ((3, 1), (4, 1), (2, 2), (3, 2), (2, 3), (3, 3), (3, 4), (4, 4)):
        rows[y][x] = "s"
    for x0, x1, top in BUILDINGS:
        for y in range(top, sky_rows - 1):
            for x in range(x0, x1):
                lit = x % 2 == 1 and y % 3 == 1 and x not in (x0, x1 - 1) and (x * 7 + y * 3) % 4 == 0
                rows[y][x] = "w" if lit else "K"
    for x, top in RAIN:
        for y in (top, top + 1):
            if rows[y][x] in "abc":
                rows[y][x] = "r"
    rows[-1] = list("g" * SCENE_W)
    out = ["".join(r) for r in rows]
    for y in range(GROUND):
        if y % 2 == 1:
            line = "".join("m" if (x + y) % 4 == 0 else "P" for x in range(SCENE_W))
        else:
            line = "".join("m" if (x + y // 2 * 2) % 4 == 2 else "P" for x in range(SCENE_W))
        if y in (2, 4):  # the glow, caught in a puddle
            line = line[:26] + "g" * 3 + line[29:] if y == 2 else line[:6] + "g" * 2 + line[8:]
        out.append(line)
    return pal, out


SCENES = {
    "office": scene(["#1c1a17", "#24211d", "#2e2a24"], "#e8dcc0", "#121110", "#c8b890", "#38342c", "#2e2a24", "#1c1a16", "#b8a888"),
    "alley": scene(["#121518", "#171c20", "#1e242a"], "#c8d4dc", "#0c0e10", "#7a8a96", "#2c343c", "#22282e", "#14181c", "#8a9aa8"),
    "precinct": scene(["#161618", "#1c1c20", "#24242a"], "#e8e4d8", "#0e0e10", "#b0b0b0", "#303036", "#28282c", "#18181a", "#c8c8c8"),
    "records": scene(["#141716", "#1a1f1c", "#222824"], "#c8d0c4", "#0c0e0d", "#8a9a8c", "#2c342e", "#242a26", "#161a18", "#9aa89a"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Dark enough that every sprite still reads.
    "idle": scene(["#141416", "#1a1a1e", "#202024"], "#6a6a70", "#0e0e10", "#3a3a40", "#2a2a30", "#26262a", "#18181b", "#55555c"),
    "working": scene(["#18181c", "#202026", "#2a2a32"], "#e8e4d8", "#101014", "#d8d0b0", "#3a3a44", "#2e2e34", "#1c1c20", "#e8e4d8"),
    "blocked": scene(["#1a0e10", "#260f14", "#3a1218"], "#ff9a9a", "#100808", "#d0303c", "#4a1a22", "#2c1418", "#1a0a0c", "#d0303c"),
    "done": scene(["#1c1e22", "#262a30", "#343a42"], "#f4f1e8", "#16181c", "#8a9098", "#30343c", "#33363c", "#202226", "#a8a8a0"),
}

# ---- icons

# 10 x 7 machine icons. F is the scene's glow, s its moon, D its cobble gaps.
TYPEWRITER = ["...ssss...", "...sDDs...", "FFFFFFFFFF", "FDFDFDFDFF", ".FDFDFDFD.", "FFFFFFFFFF", ".FF....FF."]
STREETLAMP = ["..FFFFFF..", "...ssss...", "....FF....", "....FF....", "....FF....", "....FF....", "..FFFFFF.."]
PHONE = [".FFF..FFF.", ".FFFFFFFF.", "...F..F...", "..FFFFFF..", ".FFsFFsFF.", ".FFFssFFF.", "FFFFFFFFFF"]
CASE_FILE = ["FFFF......", "FFFFFFFFFF", "FFsssssFFF", "FFFFFFFFFF", "FFFFFFFFFF", "FFFFDDFFFF", "FFFFFFFFFF"]
MAGNIFIER = ["..FFFF....", ".FssDDF...", ".FsDDDF...", ".FDDDDF...", "..FFFF....", "......FF..", ".......FF."]
SHAPES = {"office": TYPEWRITER, "alley": STREETLAMP, "precinct": PHONE, "records": CASE_FILE}

ICONS = {
    # The header's dither block.
    "dither": ({"x": "#5c5c62"}, ["x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x"]),
    # A machine: its own object, colored by the scene. Status scenes get the magnifier.
    **{
        f"machine-{name}": ({"F": pal["g"], "s": pal["s"], "D": pal["m"]}, SHAPES.get(name, MAGNIFIER))
        for name, (pal, _rows) in SCENES.items()
    },
}
