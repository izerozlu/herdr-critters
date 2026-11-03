"""Garden scenes (the sprite box behind each agent, one per machine and per status) and icons."""

# 36 x 30 grids.
SCENE_W, SCENE_H, GROUND = 36, 30, 7


def scene(
    sky: list[str], sun: str, petal: str, grass: list[str], soil: list[str], ink: str
) -> tuple[dict[str, str], list[str]]:
    """Sky bands on top, a sun, a cloud, two flowers on a grass line, then soil.

    `ink` is not drawn in the scene; it colors the machine icon.
    """
    pal = {
        "a": sky[0], "b": sky[1], "c": sky[2], "s": sun, "w": "#fffdf5", "p": petal,
        "g": grass[0], "G": grass[1], "B": soil[0], "m": soil[1], "i": ink,
    }
    rows: list[str] = []
    sky_rows = SCENE_H - GROUND
    for y in range(sky_rows):
        band = "a" if y < sky_rows * 0.45 else "b" if y < sky_rows * 0.8 else "c"
        rows.append(band * SCENE_W)

    def dot(x: int, y: int, ch: str) -> None:
        rows[y] = rows[y][:x] + ch + rows[y][x + 1 :]

    # A round sun with short rays, top right, clear of the status marks on the left.
    for x, y in ((3, 2), (4, 2), (2, 3), (3, 3), (4, 3), (5, 3), (2, 4), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5)):
        dot(SCENE_W - 1 - x, y, "s")
    for x, y in ((3, 0), (4, 0), (0, 3), (0, 4), (7, 3), (7, 4), (3, 7), (4, 7)):
        dot(SCENE_W - 1 - x, y, "s")
    # A cloud, top left.
    for x in range(6, 10):
        dot(x, 3, "w")
    for x in range(4, 12):
        dot(x, 4, "w")
    # Grass tufts on the horizon and a flower near each edge.
    for x in range(0, SCENE_W, 3):
        dot(x, sky_rows - 1, "g")
    for cx in (2, 33):
        dot(cx, sky_rows - 4, "p")
        dot(cx - 1, sky_rows - 3, "p")
        dot(cx, sky_rows - 3, "s")
        dot(cx + 1, sky_rows - 3, "p")
        dot(cx, sky_rows - 2, "p")
        dot(cx, sky_rows - 1, "G")
    rows.append("g" * SCENE_W)
    rows.append("".join("G" if x % 2 else "g" for x in range(SCENE_W)))
    for y in range(2, GROUND):
        rows.append("".join("m" if (x * 7 + y * 5) % 13 == 0 else "B" for x in range(SCENE_W)))
    return pal, rows


SCENES = {
    "greenhouse": scene(["#e8f1dc", "#ddebcd", "#d1e4be"], "#ffd166", "#f29bb6", ["#8cc56a", "#6aa84f"], ["#a07a52", "#80603e"], "#4f8a3c"),
    "barrow": scene(["#fbeee0", "#f7e2cc", "#f2d5b6"], "#ffc35a", "#e88a5a", ["#9cc46a", "#7aa84c"], ["#a07a52", "#80603e"], "#a0522d"),
    "seeds": scene(["#efe8f5", "#e6dcef", "#dccfe8"], "#ffd88a", "#b48ad8", ["#8cc06e", "#6ea452"], ["#9a7a5a", "#7a5c40"], "#7a5aa8"),
    "pond": scene(["#e2f0f5", "#d4e8f0", "#c4dfeb"], "#ffe08a", "#7ab8e0", ["#86c27a", "#64a45c"], ["#94785a", "#74593e"], "#2f7aa8"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Light enough that every outlined sprite still reads.
    "idle": scene(["#efeadb", "#e8e2d0", "#e0d9c4"], "#e8d9a0", "#d8c8d8", ["#a8b890", "#8e9e78"], ["#a89478", "#8c7a60"], "#8c8471"),
    "working": scene(["#fdf3d0", "#fbeab8", "#f8e0a0"], "#f5b82e", "#f29b6b", ["#9ccc5e", "#7fb048"], ["#9c7650", "#7d5c3a"], "#b87400"),
    "blocked": scene(["#fbe3e0", "#f7d4d0", "#f2c3be"], "#f5a07a", "#e0505a", ["#b8b46a", "#9a9850"], ["#8e6a4c", "#6e4e34"], "#cc3b3b"),
    "done": scene(["#e3f5e0", "#d4efcf", "#c4e8bf"], "#ffd166", "#f29bb6", ["#6cbf5a", "#4f9f40"], ["#9c7650", "#7d5c3a"], "#3d8b37"),
}

# ---- icons

# A machine icon per scene, 10 x 7. F is the frame (the scene's ink), S the glass
# or body (the scene's lightest sky band), s an accent (the sun), D wood or soil.
SHAPES = {
    "greenhouse": [
        "....FF....",
        "..FFSSFF..",
        "FFSSSSSSFF",
        "FSSFSSFSSF",
        "FSSFSSFSSF",
        "FFFFFFFFFF",
        "DDDDDDDDDD",
    ],
    "barrow": [
        "........DD",
        "FFFFFFFDD.",
        "FSSSSSSF..",
        ".FSSSSF...",
        "..FFFF....",
        "..FsF.D...",
        "..FFF.D...",
    ],
    "seeds": [
        ".FFFFFFFF.",
        ".FSSsSSSF.",
        ".FSsDsSSF.",
        ".FSSsSSSF.",
        ".FSSDSSSF.",
        ".FSSDSSSF.",
        ".FFFFFFFF.",
    ],
    # The watering can, also used by the status scenes.
    "pond": [
        ".FFFF.....",
        "F....F...s",
        "FFFFFFF.F.",
        "FSSSSSFF..",
        "FSSSSSF...",
        "FSSSSSF...",
        "FFFFFFF...",
    ],
}

ICONS = {
    # The header's dither block.
    "dither": ({"x": "#b8ae90"}, ["x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x"]),
    **{
        f"machine-{name}": (
            {"F": pal["i"], "S": pal["a"], "s": pal["s"], "D": pal["m"]},
            SHAPES.get(name, SHAPES["pond"]),
        )
        for name, (pal, _rows) in SCENES.items()
    },
}
