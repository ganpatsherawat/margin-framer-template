import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json

with open(r"d:\margin-framer-template\subpages-extract.json", "r", encoding="utf-8") as f:
    d1 = json.load(f)
with open(r"d:\margin-framer-template\subpages-remaining.json", "r", encoding="utf-8") as f:
    d2 = json.load(f)

all_pages = {**d1, **d2}
for path, data in all_pages.items():
    print(f"\n--- {path} Images ---")
    for img in data.get('images', []):
        src = img.get('src')
        alt = img.get('alt')
        name = src.split('?')[0].split('/')[-1]
        print(f"  {name} | alt='{alt}'")
