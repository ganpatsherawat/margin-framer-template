import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_c4():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        res = page.evaluate("""() => {
            const hero = document.querySelector('[data-framer-name="Hero"]');
            const c4 = hero.children[4];
            const items = [];
            c4.querySelectorAll('*').forEach(el => {
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                if (r.height > 80 && r.width > 200) {
                    items.push({
                        tag: el.tagName,
                        name: el.getAttribute('data-framer-name'),
                        top: Math.round(r.top + window.scrollY),
                        left: Math.round(r.left),
                        width: Math.round(r.width),
                        height: Math.round(r.height),
                        position: s.position,
                        classes: el.className
                    });
                }
            });
            return items;
        }""")
        print(json.dumps(res, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_c4()
