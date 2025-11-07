from PIL import Image, ImageOps, ImageEnhance, ImageDraw
import numpy as np

# ----------------------------------------------------------------------
# step 1: build the lightscribe-like disc from lightscribe.jpg
# ----------------------------------------------------------------------
src = Image.open("lightscribe.jpg").convert("L")
src = ImageOps.autocontrast(src, cutoff=0.5)

dark_gold = (35, 31, 18)
light_gold = (210, 190, 120)
gold_img = ImageOps.colorize(src, black=dark_gold, white=light_gold)

gold_img = ImageEnhance.Contrast(gold_img).enhance(1.6)

base_gold = np.array([69, 62, 35], dtype=float)
arr = np.array(gold_img, dtype=float)
mean_color = arr.mean(axis=(0, 1))
target = mean_color + 0.5 * (base_gold - mean_color)
scale = target / mean_color
arr = arr * scale
arr = np.clip(arr, 0, 255)

# lift blacks a bit
min_floor = 35.0
dark_mask = arr < min_floor
arr[dark_mask] = arr[dark_mask] * 0.4 + min_floor * 0.6

# small gamma lift
arr = (arr / 255.0) ** 0.93 * 255.0
arr = np.clip(arr, 0, 255).astype(np.uint8)
gold_img = Image.fromarray(arr)

w, h = gold_img.size

# disc mask
mask = Image.new("L", (w, h), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, w - 1, h - 1), fill=255)

# you can change this if your hole is a different size
hole_radius = int(min(w, h) * 0.17)
cx, cy = w // 2, h // 2
draw.ellipse((cx - hole_radius, cy - hole_radius,
              cx + hole_radius, cy + hole_radius), fill=0)

disc = Image.new("RGB", (w, h), (255, 255, 255))
disc.paste(gold_img, mask=mask)

# ----------------------------------------------------------------------
# step 2: load the real middle (hub) picture and paste it
# ----------------------------------------------------------------------
middle = Image.open("middle.png").convert("RGBA")

# scale the middle to fit where the hole is. we want it a bit bigger than the hole
# adjust middle_scale if needed
middle_scale = 0.35  # fraction of disc size; increase to make center bigger
middle_size = int(min(w, h) * middle_scale)
middle = middle.resize((middle_size, middle_size), Image.LANCZOS)

# compute top-left so it is centered
mx = cx - middle_size // 2
my = cy - middle_size // 2

# paste with alpha if the middle has transparency, else use it as is
disc.paste(middle, (mx, my), middle)

disc.save("lightscribe_ebay.jpg")
