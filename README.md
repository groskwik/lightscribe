# Lightscribe Disc Preview Generator

This project creates realistic previews of **Lightscribe gold discs** by applying colorization, contrast enhancement, and compositing steps to an input image.  

---

## 🧩 Overview

Lightscribe discs are optical media (CD/DVD) that use a laser to etch grayscale images directly onto the label side, resulting in a sepia-like image on a reflective gold surface.  
This script simulates that appearance from a regular image, producing a gold-tinted, etched-looking output suitable for product listings or previews.

---

## 📂 Files

| File | Description |
|------|--------------|
| `lightscribe.jpg` | Base artwork (the image to appear on the disc) |
| `middle.png` | Center hub (real scan of a Lightscribe disc center|
| `lightscribe_ebay.jpg` | Final generated preview |

---

## ⚙️ Requirements

Python 3.10 or later with Pillow and NumPy:

```bash
pip install pillow numpy
