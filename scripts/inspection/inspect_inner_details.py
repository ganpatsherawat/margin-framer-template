import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_inners():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            function dumpEl(el, depth = 0) {
                if (!el || depth > 3) return null;
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                return {
                    tag: el.tagName,
                    name: el.getAttribute('data-framer-name'),
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    margin: s.margin,
                    gap: s.gap,
                    fontSize: s.fontSize,
                    lineHeight: s.lineHeight,
                    fontFamily: s.fontFamily,
                    color: s.color,
                    border: s.border,
                    borderBottom: s.borderBottom,
                    text: (el.innerText || '').slice(0, 30).replace(/\\n/g, ' '),
                    children: Array.from(el.children).map(c => dumpEl(c, depth + 1))
                };
            }

            const heroClients = document.querySelector('[data-framer-name="Clients"]');
            const servicesInner = document.querySelector('[data-framer-name="Services"] > *');
            const bigNumInner = document.querySelector('[data-framer-name="Big number"] > *');
            const workInner = document.querySelector('[data-framer-name="Selected work"] > *');
            const ctaEl = Array.from(document.querySelectorAll('*')).find(el => el.innerText && el.innerText.startsWith('BOOKING FROM JANUARY 2027') && el.offsetWidth > 1000);
            const ctaInner = ctaEl ? ctaEl.firstElementChild : null;
            const footerInner = document.querySelector('[data-framer-name="Footer"] > *');

            return {
                heroClients: dumpEl(heroClients),
                servicesInner: dumpEl(servicesInner),
                bigNumInner: dumpEl(bigNumInner),
                workInner: dumpEl(workInner),
                ctaInner: dumpEl(ctaInner),
                footerInner: dumpEl(footerInner)
            };
        }""")

        with open(r"d:\margin-framer-template\inners_detail.json", "w", encoding="utf-8") as f:
            json.dump(details, f, indent=2)

        print("Saved to inners_detail.json")
        browser.close()

if __name__ == "__main__":
    inspect_inners()
