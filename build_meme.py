#!/usr/bin/env python3
"""Draw the gta6-meme-x-01 meme: Vice City sunset, the make.fun ghost as the sun,
a pink convertible cruising Ocean Drive, billboard selling make.fun.
Original joke: waited 13 years for GTA 6, called in sick, worth it.
Output: meme.png, 1024x1024, deterministic (no randomness, no network)."""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# --- sky gradient: hot pink -> orange -> gold at horizon ---
top = (255, 45, 120)
mid = (255, 110, 80)
bot = (255, 190, 90)
for y in range(560):
    if y < 280:
        t = y / 280
        c = tuple(int(top[i] + (mid[i] - top[i]) * t) for i in range(3))
    else:
        t = (y - 280) / 280
        c = tuple(int(mid[i] + (bot[i] - mid[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

# --- sun = the make.fun ghost mark (brand asset from https://make.fun/press/) ---
mark = Image.open("/tmp/mark-1024.png").convert("RGBA")
sun = mark.resize((360, 360), Image.LANCZOS)
img.paste(sun, (512 - 180, 130), sun)
d = ImageDraw.Draw(img)

# --- ocean band with sun reflection ---
for y in range(560, 700):
    t = (y - 560) / 140
    c = tuple(int(a + (b - a) * t) for a, b in zip((20, 40, 90), (10, 20, 50)))
    d.line([(0, y), (W, y)], fill=c)
for i, wdt in enumerate((180, 130, 90, 60, 40)):
    y = 580 + i * 22
    d.rectangle([512 - wdt // 2, y, 512 + wdt // 2, y + 8], fill=(255, 170, 120))

# --- art-deco building silhouettes along the horizon ---
def building(x, w, h, step=True):
    y0 = 560 - h
    d.rectangle([x, y0, x + w, 560], fill=(30, 16, 50))
    if step:
        d.rectangle([x + w * 0.25, y0 - 26, x + w * 0.75, y0], fill=(30, 16, 50))
    for wy in range(y0 + 18, 552, 34):
        for wx in range(int(x) + 12, int(x + w) - 14, 30):
            d.rectangle([wx, wy, wx + 12, wy + 16], fill=(255, 210, 110))

building(0, 150, 190)
building(150, 110, 130)
building(764, 120, 150)
building(884, 140, 210)

# --- palm silhouettes ---
def palm(x, y, s, flip=1):
    d.line([(x, y), (x + 8 * flip, y - 120 * s)], fill=(20, 10, 35), width=int(10 * s))
    cx, cy = x + 8 * flip, y - 120 * s
    # fronds: drooping quadratic curves sampled as polylines
    for ang in (-75, -40, -5, 30, 65):
        a = math.radians(ang - 90)
        dx, dy = math.cos(a) * 95 * s * flip, math.sin(a) * 40 * s
        pts = []
        for t in [i / 12 for i in range(13)]:
            px = cx + dx * t
            py = cy + dy * t + 55 * s * t * t
            pts.append((px, py))
        d.line(pts, fill=(20, 10, 35), width=int(7 * s))

palm(120, 700, 1.1)
palm(930, 700, 1.0, flip=-1)

# --- road / foreground ---
d.rectangle([0, 700, W, H], fill=(24, 12, 40))
d.polygon([(380, 700), (644, 700), (1024, H), (0, H)], fill=(38, 20, 58))
for i in range(6):
    t0 = i / 6
    y0 = 700 + t0 * t0 * 324
    w0 = 6 + t0 * 26
    d.rectangle([512 - w0 // 2, y0, 512 + w0 // 2, y0 + 10 + t0 * 22], fill=(255, 210, 110))

# --- pink convertible cruising down the road ---
cx0, cy0 = 512, 830
d.rounded_rectangle([cx0 - 190, cy0, cx0 + 190, cy0 + 78], radius=28, fill=(255, 45, 130))
d.polygon([(cx0 - 120, cy0), (cx0 - 90, cy0 - 52), (cx0 + 90, cy0 - 52), (cx0 + 120, cy0)],
          fill=(255, 120, 180))
d.rectangle([cx0 - 84, cy0 - 48, cx0 + 84, cy0 - 8], fill=(180, 230, 255))
for wx in (-120, 120):
    d.ellipse([cx0 + wx - 34, cy0 + 52, cx0 + wx + 34, cy0 + 120], fill=(12, 8, 20))
    d.ellipse([cx0 + wx - 15, cy0 + 71, cx0 + wx + 15, cy0 + 101], fill=(200, 200, 210))
d.rectangle([cx0 - 190, cy0 + 30, cx0 + 190, cy0 + 40], fill=(255, 210, 110))

# --- billboard: make.fun, worked into the scene ---
d.rectangle([36, 590, 330, 696], fill=(200, 0, 110))
d.rectangle([36, 590, 330, 696], outline=(255, 255, 255), width=4)
d.line([(52, 696), (52, 700)], fill=(20, 10, 35), width=6)
d.line([(314, 696), (314, 700)], fill=(20, 10, 35), width=6)
bf = ImageFont.truetype(BOLD, 50)
d.text((183, 604), "make.fun", font=bf, fill=(255, 255, 255), anchor="ma")
sf = ImageFont.truetype(BOLD, 18)
d.text((183, 664), "AGENTS WIN REAL MONEY", font=sf, fill=(255, 220, 240), anchor="ma")

# --- captions: big white Impact-style text, black outline ---
def caption(text, y, size):
    f = ImageFont.truetype(BOLD, size)
    d.text((512, y), text, font=f, fill=(255, 255, 255),
           anchor="ma", stroke_width=8, stroke_fill=(0, 0, 0))

caption("WAITED 13 YEARS", 28, 92)
caption("FOR GTA 6", 122, 92)
caption("CALLED IN SICK. WORTH IT.", 936, 58)

img.save("/home/hatch/workspace/makefun/gta6-meme-x-01/meme.png", "PNG")
print("saved meme.png", img.size)
