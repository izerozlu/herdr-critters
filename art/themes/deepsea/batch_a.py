"""Sprites batch A: lumen, bloom, inky, kraken, coil, pinch."""

from .kit import Critter, Part
from .paths import circle_d


def _wave(x: float, y0: float, sway: float, y1: float) -> str:
    """A hanging line that sways left and right."""
    m = (y0 + y1) / 2
    return f"M{x} {y0}Q{x - sway} {(y0 + m) / 2} {x} {m}T{x - sway * 0.4} {y1}"


def _mirror(d: str) -> str:
    """Path text flipped left to right around x = 50 (every first number of a pair is an x)."""
    out, nums, x_next = [], d.replace("M", " M ").replace("L", " L ").replace("Q", " Q ").replace("C", " C ").replace("Z", " Z ").split(), True
    for tok in nums:
        if tok.isalpha():
            out.append(tok)
            x_next = True
            continue
        out.append(f"{100 - float(tok):g}" if x_next else tok)
        x_next = not x_next
    return " ".join(out)


CRITTERS: dict[str, Critter] = {
    "lumen": Critter(  # an anglerfish, side on, facing right, with a lure on a stalk
        parts=[
            Part("M27 52L11 39Q15 52 11 65Z", tone="fin"),
            Part("M37 32Q41 20 55 27.5Q45 28 37 32Z", tone="fin"),
            Part("M55 29Q56 16 68 16.5", kind="strand", tone="fin", width=2),
            Part("M24 52C24 36 37 27 53 27C67 27 77 35 80 45L69 52L80 59C76 70 65 76 51 76C36 76 24 67 24 52Z"),
            Part("M43 60Q33 61 35 70Q42 68 48 62Z", tone="fin"),
            Part("M75 46.8L76.2 51L78.2 45.8Z M71.6 49L72.6 52.2L74.2 48Z M75 57.2L76.2 53L78.2 58.2Z "
                 "M71.6 55L72.6 51.8L74.2 56Z", kind="flat", tone="teeth"),
        ],
        colors={"body": "#8b6cff", "fin": "#5fd4ff", "teeth": "#f4f0ff", "light": "#b8fff4"},
        eyes=[(60, 41)],
        eye=4.4,
        spots=[(36, 47, 1.6), (33, 58, 1.3), (45, 70, 1.3), (60, 69, 1.1)],
        lure=(71.5, 17, 4.2),
    ),
    "bloom": Critter(  # a jellyfish
        parts=[
            Part(_wave(29, 47, 4, 77), kind="strand", tone="fin", width=2.2),
            Part(_wave(36, 48, -3, 79), kind="strand", tone="fin", width=2.2),
            Part(_wave(64, 48, 3, 79), kind="strand", tone="fin", width=2.2),
            Part(_wave(71, 47, -4, 77), kind="strand", tone="fin", width=2.2),
            Part("M45 47Q40 57 45 65Q49 72 44 79", kind="limb", tone="fin", width=3.8),
            Part("M55 47Q60 57 55 65Q51 72 56 79", kind="limb", tone="fin", width=3.8),
            Part("M24 46C24 26 36 14 50 14C64 14 76 26 76 46Q71 50 66 46Q61 50 56 46Q50.5 50 45 46Q39.5 50 34 46Q29 50 24 46Z"),
        ],
        colors={"body": "#ff7ad9", "fin": "#b98cff", "light": "#fff0fc"},
        eyes=[(42, 31), (58, 31)],
        mouth=(50, 37.5),
        eye=3.3,
        spots=[(29.5, 44, 1.2), (39.5, 45, 1.2), (50.5, 45, 1.2), (61, 45, 1.2), (71, 44, 1.2)],
    ),
    "inky": Critter(  # an octopus
        parts=[
            Part("M34 52Q25 59 22 67Q20 75 27 75", kind="limb", width=5.4),
            Part("M66 52Q75 59 78 67Q80 75 73 75", kind="limb", width=5.4),
            Part("M40 54Q36 66 32 72Q30 77 36 77", kind="limb", width=5.4),
            Part("M60 54Q64 66 68 72Q70 77 64 77", kind="limb", width=5.4),
            Part("M46 55Q46 68 43 77", kind="limb", width=5.4),
            Part("M54 55Q54 68 57 77", kind="limb", width=5.4),
            Part("M30 55C25 40 32 16 50 16C68 16 75 40 70 55Q50 60 30 55Z"),
        ],
        colors={"body": "#2fd8c0", "light": "#e0fffa"},
        eyes=[(42, 41), (58, 41)],
        mouth=(50, 48.5),
        eye=3.7,
        spots=[(40, 25, 2), (59, 23, 1.5), (55, 29.5, 1.1), (35, 33, 1.1)],
    ),
    "kraken": Critter(  # a squid, head up: a pointed mantle with fins, eight arms and two long tentacles
        parts=[
            Part("M38 56Q27 62 25 74", kind="strand", tone="arm", width=2.4),
            Part("M62 56Q73 62 75 74", kind="strand", tone="arm", width=2.4),
            Part("M25 76.5C22 76.5 21.5 72 24.5 71C27 70.5 28 75 25 76.5Z", tone="arm"),
            Part("M75 76.5C78 76.5 78.5 72 75.5 71C73 70.5 72 75 75 76.5Z", tone="arm"),
            Part("M44 14L31 24L43 28Z", tone="fin"),
            Part("M56 14L69 24L57 28Z", tone="fin"),
            Part("M41 57Q35 66 36 77", kind="limb", width=3.8),
            Part("M46 58Q43 68 44 78", kind="limb", width=3.8),
            Part("M54 58Q57 68 56 78", kind="limb", width=3.8),
            Part("M59 57Q65 66 64 77", kind="limb", width=3.8),
            Part("M50 6C58 14 63 26 62 46L38 46C37 26 42 14 50 6Z"),
            Part("M36 52C36 45 42 42 50 42C58 42 64 45 64 52C64 58 58 61 50 61C42 61 36 58 36 52Z"),
        ],
        colors={"body": "#3fb8e8", "fin": "#7fe8ff", "arm": "#5fd0f0", "light": "#d8fbff"},
        eyes=[(44, 50), (56, 50)],
        mouth=(50, 56),
        eye=3.3,
        spots=[(50, 18, 1.4), (46, 28, 1.2), (54, 33, 1.2), (47, 38, 1)],
    ),
    "coil": Critter(  # a nautilus: a striped spiral shell, a hood with the face, and short tentacles
        parts=[
            Part("M64 62Q61 70 63 78", kind="strand", tone="arm", width=2.4),
            Part("M68 63Q68 71 70 78", kind="strand", tone="arm", width=2.4),
            Part("M72 62Q75 70 78 76", kind="strand", tone="arm", width=2.4),
            Part("M76 59Q81 65 84 71", kind="strand", tone="arm", width=2.4),
            Part("M20 52C20 38 30 27 44 27C58 27 68 38 68 52C68 66 58 76 44 76C30 76 20 66 20 52Z", tone="shell"),
            Part("M44 52Q50 52 49 46Q47 39 39 41Q31 44 33 53Q35 63 46 64Q58 64 61 52Q63 39 52 33",
                 kind="line", tone="stripe", width=2.2, alpha=0.75),
            Part("M28 40L33 44M24 54L30 54M28 67L33 63M42 73L42 68M56 69L53 65", kind="line", tone="stripe", width=2, alpha=0.6),
            Part("M56 51C56 43 63 38 70 38C78 38 83 44 83 52C83 60 76 64 68 64C61 64 56 59 56 51Z"),
        ],
        colors={"body": "#ff9a5a", "shell": "#ffe2bc", "stripe": "#d0743a", "arm": "#ffb070", "light": "#fff2c8"},
        eyes=[(72, 48)],
        mouth=(77, 55),
        eye=3.4,
        spots=[(64, 58, 1), (79, 59, 1)],
    ),
    "pinch": Critter(  # a crab: a wide shell, eyes on stalks, two big claws and six legs
        parts=[
            Part("M33 60L23 66L20 77", kind="strand", tone="leg", width=2.6),
            Part("M37 64L30 71L29 79", kind="strand", tone="leg", width=2.6),
            Part("M42 66L39 73L39 79", kind="strand", tone="leg", width=2.6),
            Part(_mirror("M33 60L23 66L20 77"), kind="strand", tone="leg", width=2.6),
            Part(_mirror("M37 64L30 71L29 79"), kind="strand", tone="leg", width=2.6),
            Part(_mirror("M42 66L39 73L39 79"), kind="strand", tone="leg", width=2.6),
            Part("M32 54Q24 52 22 44", kind="limb", width=4.2),
            Part(_mirror("M32 54Q24 52 22 44"), kind="limb", width=4.2),
            Part("M14 45C11 36 17 30 24 33L21 39L27 40C27 48 18 51 14 45Z"),
            Part(_mirror("M14 45C11 36 17 30 24 33L21 39L27 40C27 48 18 51 14 45Z")),
            Part("M42 47L40 37", kind="strand", tone="leg", width=2.4),
            Part("M58 47L60 37", kind="strand", tone="leg", width=2.4),
            Part(circle_d(40, 35, 2.8), tone="stalk"),
            Part(circle_d(60, 35, 2.8), tone="stalk"),
            Part("M28 56C28 47 38 43 50 43C62 43 72 47 72 56C72 64 62 68 50 68C38 68 28 64 28 56Z"),
        ],
        colors={"body": "#ff5a4a", "leg": "#ff8a6a", "stalk": "#fff0ea", "light": "#ffe0c8"},
        eyes=[(45, 54), (55, 54)],
        mouth=(50, 61),
        eye=3,
        spots=[(40, 35, 1), (60, 35, 1)],
    ),
}
