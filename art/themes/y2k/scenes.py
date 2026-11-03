"""Y2K scenes (the sprite box behind each agent, one per machine and per status) and icons.

The look is a desktop wallpaper: a sky, a cloud, a sparkle and a glossy grass hill.
"""

# 36 x 30 grids.
SCENE_W, SCENE_H, GROUND = 36, 30, 7

CLOUD = ["..wwww...", ".wwwwwww.", "wwwwwwwww"]
SPARKLE = [(3, 1), (3, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (3, 4), (3, 5)]


def scene(sky: list[str], sparkle: str, cloud: str, grass: str, shade: str, shine: str) -> tuple[dict[str, str], list[str]]:
    """Sky bands on top, a sparkle and a cloud, a shine line, then dithered grass."""
    pal = {"a": sky[0], "b": sky[1], "c": sky[2], "s": sparkle, "w": cloud, "G": grass, "d": shade, "g": shine}
    rows: list[str] = []
    sky_rows = SCENE_H - GROUND
    for y in range(sky_rows):
        band = "a" if y < sky_rows * 0.45 else "b" if y < sky_rows * 0.8 else "c"
        rows.append(band * SCENE_W)
    # A four-point sparkle, top left, and a small one top middle.
    for x, y in [*SPARKLE, (17, 6)]:
        rows[y] = rows[y][:x] + "s" + rows[y][x + 1 :]
    for dy, line in enumerate(CLOUD):
        for dx, ch in enumerate(line):
            if ch != ".":
                y, x = 3 + dy, 24 + dx
                rows[y] = rows[y][:x] + ch + rows[y][x + 1 :]
    for y in range(GROUND):
        if y == 0:
            rows.append("g" * SCENE_W)
            continue
        rows.append("".join("d" if (x + 2 * y) % 5 == 0 else "G" for x in range(SCENE_W)))
    return pal, rows


SCENES = {
    "bliss": scene(["#2f7fe0", "#5aa2ec", "#8cc4f4"], "#ffffff", "#f4faff", "#3aa83a", "#2a8a2e", "#9be36a"),
    "ocean": scene(["#1a9cc8", "#3cbcdc", "#7ad8ec"], "#ffffff", "#eefcff", "#1a7fa8", "#126a8f", "#6ee0f2"),
    "sunset": scene(["#e05a8a", "#f08a7a", "#f8b87a"], "#fff4c8", "#ffe8e0", "#7a4ab0", "#5f3a90", "#c49bf0"),
    "grape": scene(["#6a4ac8", "#8a6ae0", "#b096f0"], "#ffffff", "#f2ecff", "#c8489a", "#a83a82", "#f29bd2"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Mid tones, so every outlined sprite still reads.
    "idle": scene(["#8a9ab0", "#a4b2c4", "#bcc8d6"], "#ffffff", "#e8eef4", "#7a8a9e", "#66768a", "#d4dde8"),
    "working": scene(["#1e8fe0", "#46b0ee", "#7ccff6"], "#ffffff", "#eefaff", "#1a9cc8", "#1482aa", "#7ae8ff"),
    "blocked": scene(["#d02a5a", "#e2507a", "#f07c9a"], "#fff0f4", "#ffe4ec", "#a8284e", "#8a1e40", "#ff9ab8"),
    "done": scene(["#3aa83a", "#62c44a", "#94dc62"], "#ffffff", "#f4ffe8", "#2a8a2e", "#1f7024", "#c8f07a"),
}

# ---- icons

ICONS = {
    # The header's dither block.
    "dither": ({"x": "#7f95b2"}, ["x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x"]),
    # A machine: a round bubble monitor on a foot. Colored per machine by the scene.
    **{
        f"machine-{name}": (
            {"F": pal["g"], "S": pal["a"], "s": pal["w"], "D": pal["d"]},
            [".FFFFFFFF.", "FSSSSSSSSF", "FSsSSSSSSF", "FSSSSSSSSF", ".FFFFFFFF.", "....DD....", "..DDDDDD.."],
        )
        for name, (pal, _rows) in SCENES.items()
    },
}
