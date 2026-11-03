"""Edo scenes (the sprite box behind each agent, one per machine and per status) and icons.

A scene is 288 x 240 (retro's 36 x 30 grid at 8 px). The sky is a bokashi, the
print's soft color fade, with a red sun; the ground, the bottom 7/30 that the
view stands sprites on, is seigaiha waves.
"""

from .kit import INK, PAPER, circle, path, rect, svg

W, H = 288, 240
GROUND = H - H * 7 // 30  # 184


def waves(sea: str, wave: str) -> str:
    """Seigaiha: rows of fans of rings, each row half hidden by the next."""
    out = []
    for row, y in enumerate(range(GROUND + 10, H + 24, 12)):
        for x in range(-24 if row % 2 else -12, W + 24, 24):
            for r, fill in ((15, sea), (10, sea), (5, sea)):
                out.append(circle(x, y, r, fill, wave, 2))
    return f'<clipPath id="g"><rect x="0" y="{GROUND}" width="{W}" height="{H - GROUND}"/></clipPath><g clip-path="url(#g)">{"".join(out)}</g>'


def scene(top: str, paper: str, sun: str, sea: str, wave: str, shore: str) -> str:
    sky = (
        f'<linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/>'
        f'<stop offset="0.45" stop-color="{paper}"/></linearGradient>'
        f'<rect width="{W}" height="{GROUND}" fill="url(#s)"/>'
    )
    return svg(W, H, sky + circle(248, 44, 22, sun, None) + waves(sea, wave) + rect(0, GROUND - 3, W, 5, shore, stroke=None))


SCENES = {
    "fuji": scene("#9fb2cc", "#ece8de", "#d0503c", "#3a5a82", "#cbd6e2", "#24406a"),
    "sakura": scene("#e8b4b8", "#f4ebe4", "#d0503c", "#c87a8a", "#f6e6e2", "#a8505e"),
    "take": scene("#b4c89a", "#eeeedf", "#d0503c", "#5a7a3a", "#d0dcb8", "#3e5a26"),
    "kaki": scene("#e8b88a", "#f4eadb", "#c23b22", "#c87a3a", "#f6e8d4", "#8a4a1e"),
    # The sprite box behind an agent shows its status; the machine scenes above
    # color the machine icons. Light paper tones, so the inked sprites read.
    "idle": scene("#cdc2a8", "#f1e9d6", "#b8a888", "#a89c80", "#e3d7bc", "#7a6e56"),
    "working": scene("#9fb8d0", "#ecefee", "#d0503c", "#2d5a86", "#c8d8e6", "#1e3e62"),
    "blocked": scene("#e8a89c", "#f6ebe6", "#c8302a", "#a83a2a", "#f0d0c8", "#7a2418"),
    "done": scene("#b4cc96", "#eef0e2", "#d0503c", "#5a8040", "#ccdcb2", "#3a5a26"),
}

# The colors each machine icon takes from its scene: (sea, wave).
_TONES = {
    "fuji": ("#3a5a82", "#cbd6e2"), "sakura": ("#c87a8a", "#f6e6e2"), "take": ("#5a7a3a", "#d0dcb8"), "kaki": ("#c87a3a", "#f6e8d4"),
    "idle": ("#a89c80", "#e3d7bc"), "working": ("#2d5a86", "#c8d8e6"), "blocked": ("#a83a2a", "#f0d0c8"), "done": ("#5a8040", "#ccdcb2"),
}


def lantern(body: str, glow: str) -> str:
    """A machine: a paper lantern (chochin), 30 x 22, in the scene's colors."""
    return svg(
        30, 22,
        rect(9, 1, 12, 3, INK, 1, None)
        + rect(9, 18, 12, 3, INK, 1, None)
        + path("M9 4 Q1 11 9 18 L21 18 Q29 11 21 4 Z", body, INK, 1.5)
        + circle(15, 11, 3.5, glow, None),
    )


ICONS = {
    # The header's mark: a red hanko seal.
    "dither": svg(12, 12, rect(1, 1, 10, 10, "#c23b22", 2, None) + rect(3.5, 3.5, 5, 5, "none", 0.5, PAPER, 1.2)),
    **{f"machine-{name}": lantern(*tone) for name, tone in _TONES.items()},
}
