"""Sprites batch B: nudi, gulper, pearl, glim, rolly, krill."""

from .kit import Critter, Part
from .paths import circle_d


def _cerata(x: float) -> str:
    """One finger on a sea slug's back."""
    return f"M{x - 3.4} 56C{x - 3.4} 48 {x - 1.2} 41 {x} 40C{x + 1.2} 41 {x + 3.4} 48 {x + 3.4} 56Z"


CRITTERS: dict[str, Critter] = {
    "nudi": Critter(  # a nudibranch: a long sea slug with two feelers and orange fingers on its back
        parts=[
            *[Part(_cerata(x), tone="cerata") for x in (44, 51, 58, 65, 72)],
            Part("M27 57L22 44", kind="strand", tone="feeler", width=2.6),
            Part("M34 55L33 42", kind="strand", tone="feeler", width=2.6),
            Part(circle_d(22, 43, 2.2), tone="cerata"),
            Part(circle_d(33, 41, 2.2), tone="cerata"),
            Part("M18 69C18 59 30 53 50 53C70 53 84 59 84 68C84 74 78 76 70 76L26 76C20 76 18 74 18 69Z"),
            Part("M24 72L79 72", kind="line", tone="stripe", width=1.8, alpha=0.8),
        ],
        colors={"body": "#9a6cff", "cerata": "#ffa040", "feeler": "#c0a0ff", "stripe": "#f4eeff", "light": "#ffe0b0"},
        eyes=[(28, 62), (38, 61)],
        mouth=(33, 67.5),
        eye=3,
        spots=[(50, 63, 1.1), (60, 64, 1.1), (70, 65, 1.1)],
    ),
    "gulper": Critter(  # a gulper eel: a huge mouth on a small head and a long whip tail with a light
        parts=[
            Part("M70 60Q84 64 82 70Q80 76 92 76", kind="strand", tone="fin", width=2.6),
            Part("M18 46C18 32 32 25 48 26C64 27 76 37 76 50C76 62 64 70 46 70C30 70 18 60 18 46Z"),
            Part("M24 50Q48 58 74 50Q68 65 46 65Q30 63 24 50Z", kind="flat", tone="mouth", alpha=0.85),
            Part("M24 50Q48 58 74 50", kind="line", tone="lip", width=1.6, alpha=0.8),
        ],
        colors={"body": "#3a9ec8", "fin": "#5ab8e0", "mouth": "#0c1430", "lip": "#a8ecff", "light": "#c8fff8"},
        eyes=[(36, 39), (48, 37)],
        eye=3.3,
        spots=[(92, 76, 1.8), (56, 33, 1), (64, 40, 1)],
    ),
    "pearl": Critter(  # a clam, open, with a pearl that has the face
        parts=[
            Part("M20 52Q22 26 50 24Q78 26 80 52Q50 46 20 52Z"),
            Part("M50 27L50 40M38 30L42 42M62 30L58 42M28 38L33 46M72 38L67 46", kind="line", tone="ridge", width=1.8, alpha=0.7),
            Part("M22 54Q50 47 78 54Q50 62 22 54Z", kind="flat", tone="inside", alpha=0.9),
            Part(circle_d(50, 47, 11), tone="pearl"),
            Part("M18 56Q50 50 82 56Q80 76 50 77Q20 76 18 56Z", tone="shell"),
            Part("M30 62Q50 58 70 62M34 69Q50 66 66 69", kind="line", tone="ridge", width=1.8, alpha=0.7),
        ],
        colors={"body": "#a07ae8", "shell": "#a07ae8", "ridge": "#e0d0ff", "inside": "#2a1848", "pearl": "#fff0fa", "light": "#ffffff"},
        eyes=[(46, 45), (54, 45)],
        mouth=(50, 50.5),
        eye=2.4,
    ),
    "glim": Critter(  # a lanternfish, side on, facing right, with a row of lights on its belly
        parts=[
            Part("M26 52L12 41Q16 52 12 63Z", tone="fin"),
            Part("M44 37Q50 27 59 36Z", tone="fin"),
            Part("M22 52C26 40 40 34 56 36C70 37 80 44 82 52C80 60 70 66 56 66C40 66 26 62 22 52Z"),
            Part("M48 64L44 73L56 65Z", tone="fin"),
        ],
        colors={"body": "#4a7cff", "fin": "#7aa8ff", "light": "#7ffcff"},
        eyes=[(67, 47)],
        mouth=(76, 56),
        eye=4.3,
        spots=[(34, 57, 1.3), (40, 59.5, 1.3), (46, 60.5, 1.3), (52, 61, 1.3), (58, 61, 1.3), (64, 60, 1.3)],
    ),
    "rolly": Critter(  # a giant isopod, from the front: a dome of plates, two feelers and many short legs
        parts=[
            Part("M42 37Q36 30 30 28", kind="strand", tone="leg", width=2.4),
            Part("M58 37Q64 30 70 28", kind="strand", tone="leg", width=2.4),
            *[Part(f"M{x} 68L{x - 1.5} 78", kind="strand", tone="leg", width=2.6) for x in (27, 35, 43, 51, 59, 67, 75)],
            Part("M18 70C18 48 32 34 50 34C68 34 82 48 82 70Q50 74 18 70Z"),
            Part("M21 59Q50 53 79 59M19 66Q50 60 81 66", kind="line", tone="plate", width=1.8, alpha=0.75),
        ],
        colors={"body": "#b0a0e0", "leg": "#8a7ac8", "plate": "#f0eaff", "light": "#f4f0ff"},
        eyes=[(42, 47), (58, 47)],
        mouth=(50, 53),
        eye=3.4,
    ),
    "krill": Critter(  # a krill, side on, facing left: a curled pink body, a horn, feelers and legs
        parts=[
            Part("M23 46Q10 50 4 60", kind="strand", tone="leg", width=2),
            Part("M25 44L11 34", kind="strand", tone="horn", width=2.4),
            *[Part(f"M{x} 58L{x - 2} 72", kind="strand", tone="leg", width=2.4) for x in (32, 39, 46, 53, 60)],
            Part("M68 60L76 74L86 64Z", tone="tail"),
            Part("M20 47C23 38 40 36 56 40C68 43 76 50 78 58C79 64 74 67 70 62C64 57 56 57 46 59C33 61 21 57 20 47Z"),
            Part("M44 40Q48 48 46 58M54 41Q58 49 56 57M64 46Q66 52 63 58", kind="line", tone="plate", width=1.6, alpha=0.6),
        ],
        colors={"body": "#ff7a9a", "leg": "#ffa0b8", "horn": "#fff0f4", "tail": "#ff96b0", "plate": "#ffe0ea", "light": "#7ffcff"},
        eyes=[(30, 45)],
        mouth=(23, 51),
        eye=3.4,
        spots=[(40, 54, 1.1), (50, 52, 1.1), (60, 53, 1.1)],
    ),
}
