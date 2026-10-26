import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_exact_hero_layout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        data = page.evaluate("""() => {
            const hero = document.querySelector('[data-framer-name="Hero"]');
            if (!hero) return { error: "Hero not found" };

            const r = hero.getBoundingClientRect();
            const s = window.getComputedStyle(hero);

            const children = Array.from(hero.children).map((c, i) => {
                const cr = c.getBoundingClientRect();
                const cs = window.getComputedStyle(c);
                return {
                    i,
                    tag: c.tagName,
                    name: c.getAttribute('data-framer-name'),
                    className: c.className.slice(0, 30),
                    top: Math.round(cr.top + window.scrollY),
                    height: Math.round(cr.height),
                    width: Math.round(cr.width),
                    padding: cs.padding,
                    margin: cs.margin,
                    gap: cs.gap,
                    display: cs.display,
                    position: cs.position,
                    text: (c.innerText || '').slice(0, 60).replace(/\\n/g, ' ')
                };
            });

            return {
                hero: {
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    gap: s.gap
                },
                children
            };
        }""")

        print(json.dumps(data, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_exact_hero_layout()
