import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_hero_visual():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            // Find all children in Hero
            const hero = document.querySelector('[data-framer-name="Hero"]');
            if (!hero) return { error: "Hero not found" };

            function getInfo(el) {
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                return {
                    tag: el.tagName,
                    framerName: el.getAttribute('data-framer-name'),
                    top: Math.round(r.top + window.scrollY),
                    left: Math.round(r.left),
                    width: Math.round(r.width),
                    height: Math.round(r.height),
                    position: s.position,
                    display: s.display,
                    zIndex: s.zIndex,
                    overflow: s.overflow,
                    backgroundColor: s.backgroundColor,
                    borderRadius: s.borderRadius,
                    boxShadow: s.boxShadow,
                    border: s.border,
                    className: el.className
                };
            }

            return {
                hero: getInfo(hero),
                children: Array.from(hero.children).map(getInfo),
                // Find the decision card
                decisionCard: (() => {
                    const el = Array.from(document.querySelectorAll('*')).find(e => e.innerText && e.innerText.includes('The not-now list') && e.getAttribute('data-framer-name') === 'Decision record' || e.getAttribute('data-framer-name') === 'Card');
                    return el ? getInfo(el) : null;
                })()
            };
        }""")

        print(json.dumps(details, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_hero_visual()
