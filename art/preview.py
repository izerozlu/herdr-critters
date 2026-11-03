"""Draw a preview sheet of sprites in every pose, each on its status scene.

Run from the repo root after generate.py:
    uv run --no-project --with pillow art/preview.py [out.png] [name ...]
Without names it draws every sprite. CRITTERS_ART=<dir> reads another art folder. Default output: art/preview-sprites.png
"""

import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ART = Path(os.environ.get("CRITTERS_ART", ROOT / "mods" / "herdr-critters" / "themes" / "retro" / "art"))
FONT = ROOT / "mods" / "herdr-critters" / "fonts" / "Silkscreen-Regular.ttf"
STATUSES = ("idle", "working", "blocked", "done")
RECT = re.compile(r'<rect x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)" fill="(#\w+)"/>')


def raster(path: Path, scale: int) -> Image.Image:
    text = path.read_text()
    w, h = map(int, re.search(r'viewBox="0 0 (\d+) (\d+)"', text).groups())
    im = Image.new("RGBA", (w * scale, h * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    for x, y, rw, rh, fill in RECT.findall(text):
        x, y, rw, rh = map(int, (x, y, rw, rh))
        draw.rectangle([x * scale, y * scale, (x + rw) * scale - 1, (y + rh) * scale - 1], fill=fill)
    return im


def main() -> None:
    args = sys.argv[1:]
    out = Path(args.pop(0)) if args and args[0].endswith(".png") else ROOT / "art" / "preview-sprites.png"
    names = args or sorted({p.name.split("-")[1] for p in ART.glob("sprite-*-idle.svg")})
    scenes = {s: raster(ART / f"scene-{s}.svg", 5) for s in STATUSES}  # 180 x 150
    cw, ch, lw, top = 200, 170, 90, 40
    font = ImageFont.truetype(str(FONT), 16)
    sheet = Image.new("RGBA", (lw + len(STATUSES) * cw, top + len(names) * ch), "#12131b")
    draw = ImageDraw.Draw(sheet)
    for c, status in enumerate(STATUSES):
        draw.text((lw + c * cw + 50, 10), status.upper(), font=font, fill="#e8922e")
    for r, name in enumerate(names):
        draw.text((8, top + r * ch + 65), name.upper(), font=font, fill="#b49be0")
        for c, status in enumerate(STATUSES):
            x, y = lw + c * cw, top + r * ch
            sheet.paste(scenes[status], (x, y), scenes[status])
            sprite = raster(ART / f"sprite-{name}-{status}.svg", 6)  # 120 x 96
            sheet.paste(sprite, (x + 30, y + 150 - 35 - 96 + 6), sprite)
    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
