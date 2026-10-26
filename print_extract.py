import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json

with open(r"d:\margin-framer-template\original-extract.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== PAGE TITLE ===")
print(data.get("title"))

print("\n=== LINKS ===")
for l in data["links"]:
    t = l['text'].replace('\n', ' ')
    print(f"{t} -> {l['href']}")

print("\n=== IMAGES ===")
for img in data["images"]["imgs"]:
    print(f"ALT: {img.get('alt')} | SRC: {img.get('src')}")

print("\n=== TOKENS ===")
print(json.dumps(data["tokens"], indent=2))
