import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_sections():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        # Get the full page innerText
        body_text = page.evaluate("() => document.body.innerText")
        print("=== BODY TEXT ===")
        print(body_text)

        # Download all original images to public/assets/
        import os, urllib.request
        os.makedirs(r"d:\margin-framer-template\public\images", exist_ok=True)
        
        imgs = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('img')).map(img => ({
                src: img.src,
                alt: img.alt
            }));
        }""")
        
        print("\n=== DOWNLOADING IMAGES ===")
        for i, img in enumerate(imgs):
            src = img['src']
            if src.startswith('http'):
                # Extract clean filename or hash
                base_name = src.split('?')[0].split('/')[-1]
                if not base_name.endswith(('.jpg', '.png', '.webp', '.svg')):
                    base_name += '.jpg'
                dest = os.path.join(r"d:\margin-framer-template\public\images", base_name)
                try:
                    req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
                        f.write(resp.read())
                    print(f"Downloaded {base_name} ({img.get('alt')[:30]})")
                except Exception as e:
                    print(f"Failed {src}: {e}")

        browser.close()

if __name__ == "__main__":
    inspect_sections()
