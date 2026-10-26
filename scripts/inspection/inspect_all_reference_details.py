import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        data = page.evaluate("""() => {
            function getStyles(sel) {
                const el = document.querySelector(sel);
                if (!el) return null;
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                return {
                    sel,
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    margin: s.margin,
                    gap: s.gap,
                    fontSize: s.fontSize,
                    lineHeight: s.lineHeight,
                    color: s.color,
                    backgroundColor: s.backgroundColor
                };
            }

            return {
                hero: getStyles('[data-framer-name="Hero"]'),
                heroCopy: getStyles('[data-framer-name="Copy"]'),
                heroShowcase: getStyles('[data-framer-name="Showcase"]'),
                heroClients: getStyles('[data-framer-name="Clients"]'),
                services: getStyles('[data-framer-name="Services"]'),
                bigNumber: getStyles('[data-framer-name="Big number"]'),
                selectedWork: getStyles('[data-framer-name="Selected work"]'),
                photoQuote: getStyles('[data-framer-name="Photo quote"]'),
                cta: getStyles('[data-framer-name="Call to action"]'),
                footer: getStyles('[data-framer-name="Footer"]')
            };
        }""")

        print(json.dumps(data, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_all()
