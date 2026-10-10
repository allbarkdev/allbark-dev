#!/usr/bin/env python3
"""Render a 1200x630 Open Graph card for a Bark Blog post.

GitHub Pages can't generate images, so we render them when a post is drafted
and commit the PNG next to the post's screenshots.

    python3 _tools/og_image.py _posts/2026-10-12-w41-some-slug.md
    python3 _tools/og_image.py --default        # assets/devlog/og-default.png

Reads the post's front matter: title, week, date, image (where to write the
PNG) and og_shot (optional; a real screenshot from the post to show on the card).
Needs only Pillow (pip install pillow). Fonts are Inter (OFL), bundled in _tools/fonts.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path(__file__).resolve().parent / "fonts"
W, H = 1200, 630
BG = (244, 236, 216)        # --bg
CARD = (251, 246, 234)      # --card
INK = (58, 47, 31)          # --ink
MUTED = (111, 96, 71)       # --muted
RULE = (216, 201, 168)      # --rule
ACCENT = (74, 122, 44)      # --accent
PAD = 72


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def front_matter(path):
    text = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        sys.exit(f"{path}: no front matter")
    data = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv:
            val = kv.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1].replace('\\"', '"')
            data[kv.group(1)] = val
    return data


def paw(size, color):
    """The All Bark paw, drawn the same way as assets/devlog/paw.svg (64-unit grid)."""
    s = size / 64
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    def toe(cx, cy, rx, ry, angle):
        box = int(max(rx, ry) * 2 * s) + 4
        t = Image.new("RGBA", (box, box), (0, 0, 0, 0))
        ImageDraw.Draw(t).ellipse(
            [box / 2 - rx * s, box / 2 - ry * s, box / 2 + rx * s, box / 2 + ry * s], fill=color
        )
        t = t.rotate(-angle, resample=Image.BICUBIC)
        layer.alpha_composite(t, (int(cx * s - box / 2), int(cy * s - box / 2)))

    toe(14, 27, 6.5, 8.5, -18)
    toe(25, 15, 6.5, 9, 0)
    toe(39, 15, 6.5, 9, 0)
    toe(50, 27, 6.5, 8.5, 18)
    d = ImageDraw.Draw(layer)
    d.ellipse([16 * s, 31 * s, 48 * s, 57 * s], fill=color)
    return layer


def wrap(draw, text, fnt, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        trial = f"{line} {w}".strip()
        if draw.textlength(trial, font=fnt) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def fit_title(draw, text, width, max_lines=4):
    for size in range(76, 39, -4):
        fnt = font("InterDisplay-Bold.otf", size)
        lines = wrap(draw, text, fnt, width)
        if len(lines) <= max_lines:
            return fnt, lines, size
    fnt = font("InterDisplay-Bold.otf", 40)
    lines = wrap(draw, text, fnt, width)[:max_lines]
    lines[-1] = lines[-1].rstrip(".,;:") + "…"
    return fnt, lines, 40


def rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, img.width - 1, img.height - 1], radius, fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def render(title, week=None, when=None, shot=None, out=None):
    title = re.sub(r"(\w)'", "\\1\u2019", title)  # typographic apostrophes, like the page
    img = Image.new("RGBA", (W, H), BG + (255,))
    d = ImageDraw.Draw(img)

    text_right = W - PAD
    if shot:
        # A real screenshot, cropped from the top and bleeding off the bottom edge.
        s = Image.open(shot).convert("RGBA")
        target_w = 340 if s.height > s.width else 520
        s = s.resize((target_w, round(s.height * target_w / s.width)), Image.LANCZOS)
        visible = H - 56
        s = s.crop((0, 0, s.width, min(s.height, visible + 40)))
        frame = Image.new("RGBA", (s.width + 16, s.height + 16), RULE + (255,))
        frame = rounded(frame, 30)
        frame.alpha_composite(rounded(s, 24), (8, 8))
        x = W - PAD + 16 - frame.width
        img.alpha_composite(frame, (x, 56))
        text_right = x - 48
    else:
        big = paw(420, ACCENT + (38,))
        img.alpha_composite(big, (W - 420 - 24, H - 420 + 40))
        text_right = W - 330

    # Brand line
    img.alpha_composite(paw(44, ACCENT + (255,)), (PAD, PAD - 4))
    d.text((PAD + 56, PAD + 18), "THE BARK BLOG", font=font("Inter-Medium.otf", 26), fill=ACCENT, anchor="lm")

    # Title
    fnt, lines, size = fit_title(d, title, text_right - PAD)
    lh = int(size * 1.14)
    y = PAD + 88
    for ln in lines:
        d.text((PAD, y), ln, font=fnt, fill=INK)
        y += lh

    # Footer: dog-tag week badge, date, domain
    fy = H - PAD - 4
    x = PAD
    small = font("Inter-Medium.otf", 24)
    if week:
        label = week.split("-")[-1]
        tw = d.textlength(label, font=small)
        d.rounded_rectangle([x, fy - 22, x + tw + 52, fy + 22], 22, fill=ACCENT)
        d.ellipse([x + 14, fy - 5, x + 24, fy + 5], fill=BG)
        d.text((x + 34, fy), label, font=small, fill=CARD, anchor="lm")
        x += tw + 72
    footer = "allbark.dev/devlog"
    if when:
        footer = f"{when:%B} {when.day}, {when.year}  ·  {footer}"
    d.text((x, fy), footer, font=small, fill=MUTED, anchor="lm")

    out.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(out, optimize=True)
    print(f"wrote {out.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post", nargs="?", help="path to a _posts/*.md file")
    ap.add_argument("--default", action="store_true", help="render the devlog's default card")
    args = ap.parse_args()

    if args.default:
        render("What we built this week, what broke, and how we fixed it.",
               out=ROOT / "assets/devlog/og-default.png")
        return
    if not args.post:
        ap.error("give a post path or --default")

    fm = front_matter(args.post)
    for key in ("title", "image"):
        if not fm.get(key):
            sys.exit(f"{args.post}: front matter needs '{key}'")
    when = None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", fm.get("date") or Path(args.post).name)
    if m:
        when = date(*map(int, m.groups()))
    shot = ROOT / fm["og_shot"].lstrip("/") if fm.get("og_shot") else None
    render(fm["title"], fm.get("week"), when, shot, ROOT / fm["image"].lstrip("/"))


if __name__ == "__main__":
    main()
