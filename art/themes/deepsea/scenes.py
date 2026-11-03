"""Deepsea scenes (the sprite box behind each agent, one per machine and per status) and icons."""

# 36 x 30 grids, the same frame as retro so sprites sit on the seabed.
SCENE_W, SCENE_H, GROUND = 36, 30, 7


def put(rows: list[str], x: int, y: int, ch: str) -> None:
    rows[y] = rows[y][:x] + ch + rows[y][x + 1 :]


def scene(water: list[str], snow: str, sand: str, rock: str, glow: str) -> tuple[dict[str, str], list[str]]:
    """Water bands on top with drifting specks and a bubble, coral at the sides, then the seabed."""
    pal = {"a": water[0], "b": water[1], "c": water[2], "s": snow, "B": sand, "m": rock, "g": glow}
    rows: list[str] = []
    water_rows = SCENE_H - GROUND
    for y in range(water_rows):
        band = "a" if y < water_rows * 0.4 else "b" if y < water_rows * 0.75 else "c"
        rows.append(band * SCENE_W)
    # Marine snow: single specks drifting down.
    for x, y in ((4, 3), (13, 1), (22, 4), (9, 9), (27, 2), (18, 12), (6, 15), (25, 10)):
        put(rows, x, y, "s")
    # Tiny bubbles rising on the right.
    for x, y in ((32, 9), (31, 5)):
        put(rows, x, y, "s")
    # Glowing coral: a branch on the left and a tuft on the right.
    for x, y in ((2, 17), (2, 18), (2, 19), (3, 20), (3, 21), (3, 22), (4, 19), (4, 18), (1, 20), (0, 19)):
        put(rows, x, y, "g")
    for x, y in ((32, 20), (33, 19), (33, 21), (33, 22), (34, 20), (34, 21), (35, 19)):
        put(rows, x, y, "g")
    # The seabed: a sand line, then sand with scattered pebbles.
    rows.append("B" * SCENE_W)
    for y in range(1, GROUND):
        rows.append("".join("m" if (x * 7 + y * 5) % 11 == 0 else "B" if (x + y) % 2 else "m" if y > 3 else "B" for x in range(SCENE_W)))
    return pal, rows


SCENES = {
    "abyss": scene(["#0a0f24", "#0c1430", "#0f1a3c"], "#7ffcff", "#1a2440", "#10182c", "#3ff0ff"),
    "reef": scene(["#140c24", "#1c1030", "#26143e"], "#ffb8f4", "#2a1c40", "#1a1028", "#ff70c8"),
    "vent": scene(["#1a0e14", "#24121a", "#301622"], "#ffd27a", "#2e1c20", "#1c1014", "#ff8a3a"),
    "trench": scene(["#081418", "#0a1c22", "#0c242c"], "#9fffd8", "#18302e", "#0e1e1c", "#3fd8a8"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Dark enough that every sprite still reads.
    "idle": scene(["#0c0f1c", "#101426", "#141a30"], "#7a86a8", "#1e2438", "#141826", "#5a6688"),
    "working": scene(["#06182a", "#08223a", "#0a2e4a"], "#9ff8ff", "#123448", "#0a2232", "#3ff0ff"),
    "blocked": scene(["#1e0818", "#2a0c22", "#38102e"], "#ffb0d0", "#3a1430", "#240a1e", "#ff4f8b"),
    "done": scene(["#061a16", "#08261e", "#0a3428"], "#c8ffe0", "#14382c", "#0a241c", "#6bffb0"),
}

# ---- icons

ICONS = {
    # The header's dither block.
    "dither": ({"x": "#1f6f80"}, ["x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x"]),
    # A machine: a small submarine. Colored per machine by the scene's glow.
    **{
        f"machine-{name}": (
            {"F": pal["g"], "s": pal["s"]},
            [".s....FF..", "s.....F...", "F..FFFFFF.", "FFFsFsFsFF", "FFFFFFFFFF", "F..FFFFFF.", ".........."],
        )
        for name, (pal, _rows) in SCENES.items()
    },
}
