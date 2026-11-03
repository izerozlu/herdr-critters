"""Retro scenes (the sprite box behind each agent, one per machine and per status) and icons."""

# 36 x 30 grids.
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
