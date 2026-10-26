import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json, os, urllib.request
from playwright.sync_api import sync_playwright

subpages = [
    "/work",
    "/insights",
    "/contact",
    "/style-guide",
    "/services/go-to-market",
    "/services/advisory",
    "/work/fernhill",
    "/work/oakmont-health",
    "/work/tidewater"
]

def crawl_fast():
    results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for path in subpages:
            url = f"https://essential-time-088020.framer.app{path}"
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=10000)
                page.wait_for_timeout(2000)
                
                title = page.title()
                text = page.evaluate("() => document.body.innerText")
                imgs = page.evaluate("""() => {
                    return Array.from(document.querySelectorAll('img')).map(img => ({
                        src: img.src,
                        alt: img.alt
                    }));
                }""")
                
                for img in imgs:
                    src = img['src']
                    if src.startswith('http'):
                        base_name = src.split('?')[0].split('/')[-1]
                        if not base_name.endswith(('.jpg', '.png', '.webp', '.svg')):
                            base_name += '.jpg'
                        dest = os.path.join(r"d:\margin-framer-template\public\images", base_name)
                        if not os.path.exists(dest):
                            try:
                                req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
                                with urllib.request.urlopen(req) as resp, open(dest, 'wb') as f:
                                    f.write(resp.read())
                                print(f"Saved: {base_name}")
                            except Exception as e:
                                pass

                results[path] = {
                    "title": title,
                    "text_lines": [line.strip() for line in text.split('\n') if line.strip()],
                    "images": imgs
                }
                print(f"Crawled {path} ({title})")
            except Exception as e:
                print(f"Error {path}: {e}")
            finally:
                page.close()
        browser.close()

    with open(r"d:\margin-framer-template\subpages-remaining.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("Remaining subpages crawled.")

if __name__ == "__main__":
    crawl_fast()
