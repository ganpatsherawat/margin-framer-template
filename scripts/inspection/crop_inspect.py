import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image

# ref-1440.png is at 2x scale, so y=616 -> 616*2 = 1232, height 515*2 = 1030
im = Image.open(r"d:\margin-framer-template\ref-1440.png")
print("Full image size:", im.size)

# Crop hero showcase (242*2, 616*2, (242+956)*2, (616+515)*2)
box = (int(242*2), int(616*2), int((242+956)*2), int((616+515)*2))
crop = im.crop(box)
crop.save(r"d:\margin-framer-template\ref-hero-showcase.png")
print("Saved ref-hero-showcase.png with size", crop.size)

# Also crop header and hero copy
box_top = (0, 0, im.size[0], int(616*2))
crop_top = im.crop(box_top)
crop_top.save(r"d:\margin-framer-template\ref-hero-top.png")
print("Saved ref-hero-top.png with size", crop_top.size)
