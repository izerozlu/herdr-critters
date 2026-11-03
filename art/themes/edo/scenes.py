"""Edo scenes (the sprite box behind each agent, one per machine and per status) and icons."""

# 36 x 30 grids.
SCENE_W, SCENE_H, GROUND = 36, 30, 7

# A seigaiha wave tile, 6 wide and 3 high; every other band shifts by 3.
WAVE = ["..WW..", ".W..W.", "W....W"]


def scene(sky: list[str], sun: str, sea: str, wave: str, shore: str) -> tuple[dict[str, str], list[str]]:
    """Paper sky bands on top, a round sun, a shore line, then seigaiha waves."""
    pal = {"a": sky[0], "b": sky[1], "c": sky[2], "s": sun, "B": sea, "W": wave, "g": shore}
    rows: list[str] = []
    sky_rows = SCENE_H - GROUND
    for y in range(sky_rows):
        band = "a" if y < sky_rows * 0.45 else "b" if y < sky_rows * 0.8 else "c"
        rows.append(band * SCENE_W)
    # The sun, a disc rising from the top right corner, clear of the pose marks.
    for y, (x0, x1) in enumerate(((32, 36), (32, 36), (33, 36), (34, 36))):
        rows[y] = rows[y][:x0] + "s" * (x1 - x0) + rows[y][x1:]
    rows[-1] = "g" * SCENE_W
    for y in range(GROUND):
        offset = 0 if (y // 3) % 2 == 0 else 3
        line = WAVE[y % 3]
        rows.append("".join("B" if line[(x + offset) % 6] == "." else "W" for x in range(SCENE_W)))
    return pal, rows


SCENES = {
    "sakura": scene(["#f6e6e2", "#f2d8d4", "#ecc8c6"], "#d0503c", "#c87a8a", "#f6e6e2", "#a8505e"),
    "fuji": scene(["#e8ecf0", "#dbe2ea", "#cbd6e2"], "#d0503c", "#3a5a82", "#cbd6e2", "#24406a"),
    "take": scene(["#eaeedc", "#dfe6cc", "#d0dcb8"], "#d0503c", "#5a7a3a", "#d0dcb8", "#3e5a26"),
    "kaki": scene(["#f6e8d4", "#f2dcc0", "#eccca8"], "#c23b22", "#c87a3a", "#f6e8d4", "#8a4a1e"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Light paper tones, so the inked sprites read.
    "idle": scene(["#f1e9d6", "#ebe1ca", "#e3d7bc"], "#b8a888", "#a89c80", "#e3d7bc", "#7a6e56"),
    "working": scene(["#e6edf2", "#d8e4ee", "#c8d8e6"], "#d0503c", "#2d5a86", "#c8d8e6", "#1e3e62"),
    "blocked": scene(["#f6e2dc", "#f0d0c8", "#e8bcb2"], "#c8302a", "#a83a2a", "#f0d0c8", "#7a2418"),
    "done": scene(["#e8eedc", "#dbe6c8", "#ccdcb2"], "#d0503c", "#5a8040", "#ccdcb2", "#3a5a26"),
}

# ---- icons

ICONS = {
    # The header's dither block.
    "dither": ({"x": "#8a7a5e"}, ["x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x", "x.x.x.", ".x.x.x"]),
    # A machine: a paper lantern (chochin) with a sun mark. Colored per machine by the scene's sea.
    **{
        f"machine-{name}": (
            {"F": pal["g"], "S": pal["B"], "s": pal["a"], "D": "#2a2420"},
            ["..DDDDDD..", ".FSSSSSSF.", "FSSSssSSSF", "FSSssssSSF", "FSSSssSSSF", ".FSSSSSSF.", "..DDDDDD.."],
        )
        for name, (pal, _rows) in SCENES.items()
    },
}
