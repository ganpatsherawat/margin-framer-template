import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        data = page.evaluate("""() => {
            function getInfo(sel) {
                const el = typeof sel === 'string' ? document.querySelector(sel) : sel();
                if (!el) return null;
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                return {
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    margin: s.margin,
                    gap: s.gap,
                    fontSize: s.fontSize,
                    lineHeight: s.lineHeight
                };
            }

            return {
                hero: getInfo('[data-framer-name="Hero"]'),
                heroCopy: getInfo('[data-framer-name="Copy"]'),
                heroShowcase: getInfo('[data-framer-name="Showcase"]'),
                heroClients: getInfo('[data-framer-name="Clients"]'),
                services: getInfo('[data-framer-name="Services"]'),
                bigNum: getInfo('[data-framer-name="Big number"]'),
                work: getInfo('[data-framer-name="Selected work"]'),
                photoQuote: getInfo('[data-framer-name="Photo quote"]'),
                cta: getInfo(() => Array.from(document.querySelectorAll('*')).find(el => el.innerText && el.innerText.startsWith('BOOKING FROM JANUARY 2027') && el.offsetWidth > 300)),
                footer: getInfo('[data-framer-name="Footer"]')
            };
        }""")

        print(json.dumps(data, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_mobile()
