import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
from PIL import Image

def compare_images():
    ref = Image.open(r"d:\margin-framer-template\ref-1440.png")
    dup = Image.open(r"d:\margin-framer-template\dup-1440.png")
    print(f"ref-1440: {ref.size}")
    print(f"dup-1440: {dup.size}")

    ref_m = Image.open(r"d:\margin-framer-template\ref-mobile.png")
    dup_m = Image.open(r"d:\margin-framer-template\dup-mobile.png")
    print(f"ref-mobile: {ref_m.size}")
    print(f"dup-mobile: {dup_m.size}")

if __name__ == "__main__":
    compare_images()
