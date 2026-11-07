#!/usr/bin/env python3
"""static/og-images/<slug>.png 이 없는 글에 1200x630 공유 이미지 생성 (기존 5월 카드 스타일).
사용: python3 scripts/make_og_images.py [--force slug ...]"""
import glob, os, re, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "og-images")
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
W, H = 1200, 630
BG, RED, WHITE, GRAY = (18, 18, 18), (229, 57, 53), (255, 255, 255), (150, 150, 150)


def font(size, bold=True):
    # AppleSDGothicNeo.ttc index: 0 Regular … 6 Bold (확인값 아님 → 실패 시 0)
    for idx in ((6, 4, 0) if bold else (0,)):
        try:
            return ImageFont.truetype(FONT, size, index=idx)
        except Exception:
            pass
    return ImageFont.load_default()


def fm(text, key):
    m = re.search(rf"^{key}:\s*(.+)$", text, re.M)
    return m.group(1).strip().strip('"\'') if m else ""


def wrap(draw, text, f, width):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=f) > width and cur:
            # 단어 중간 끊김 줄이기: 마지막 공백에서 자름
            cut = cur.rfind(" ")
            if cut > len(cur) * 0.5:
                lines.append(cur[:cut]); cur = cur[cut + 1:] + ch
            else:
                lines.append(cur); cur = ch
        else:
            cur += ch
    if cur:
        lines.append(cur)
    return lines


def render(title, category, date, path):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 14, H], fill=RED)
    if category:
        cf = font(30)
        tw = d.textlength(category, font=cf)
        d.rounded_rectangle([80, 70, 80 + tw + 40, 70 + 52], radius=12, fill=RED)
        d.text((100, 78), category, font=cf, fill=WHITE)
    size, tf, lines = 64, None, []
    while size > 40:
        tf = font(size)
        lines = wrap(d, title, tf, W - 160)
        if len(lines) <= 4:
            break
        size -= 4
    lines = lines[:4]
    y = 170
    for ln in lines:
        d.text((80, y), ln.strip(), font=tf, fill=WHITE)
        y += int(size * 1.35)
    sf = font(28, bold=False)
    d.text((80, H - 70), date, font=sf, fill=GRAY)
    d.text((W - 80 - d.textlength("tomworld", font=sf), H - 70), "tomworld", font=sf, fill=GRAY)
    im.save(path, optimize=True)


def main():
    force = set(sys.argv[2:]) if len(sys.argv) > 1 and sys.argv[1] == "--force" else set()
    made = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content", "posts", "*.md"))):
        slug = os.path.basename(f)[:-3]
        out = os.path.join(OUT, slug + ".png")
        if os.path.exists(out) and slug not in force:
            continue
        t = open(f, encoding="utf-8").read().split("---")[1]
        cat = re.findall(r'"([^"]+)"', fm(t, "categories")) or [fm(t, "categories").strip("[]")]
        render(fm(t, "title"), cat[0] if cat else "", fm(t, "date")[:10], out)
        made.append(slug)
    print(len(made), "made"); [print(" ", s) for s in made]


if __name__ == "__main__":
    main()
