import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_mobile_inners():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        data = page.evaluate("""() => {
            function dumpChildren(sel) {
                const el = typeof sel === 'string' ? document.querySelector(sel) : sel();
                if (!el) return null;
                return Array.from(el.children).map(c => {
                    const r = c.getBoundingClientRect();
                    const s = window.getComputedStyle(c);
                    return {
                        tag: c.tagName,
                        name: c.getAttribute('data-framer-name'),
                        top: Math.round(r.top + window.scrollY),
                        height: Math.round(r.height),
                        width: Math.round(r.width),
                        padding: s.padding,
                        margin: s.margin,
                        gap: s.gap,
                        fontSize: s.fontSize,
                        lineHeight: s.lineHeight,
                        text: (c.innerText || '').slice(0, 40).replace(/\\n/g, ' ')
                    };
                });
            }

            return {
                heroShowcase: dumpChildren('[data-framer-name="Showcase"]'),
                servicesInner: dumpChildren('[data-framer-name="Services"] > *'),
                servicesList: dumpChildren('[data-framer-name="Services list"]'),
                bigNumInner: dumpChildren('[data-framer-name="Big number"] > *'),
                workInner: dumpChildren('[data-framer-name="Selected work"] > *'),
                workRows: dumpChildren('[data-framer-name="Selected work"] [data-framer-name*="Inner"] > div:last-child'),
                ctaInner: dumpChildren(() => {
                    const el = Array.from(document.querySelectorAll('*')).find(x => x.innerText && x.innerText.startsWith('BOOKING FROM JANUARY 2027') && x.offsetWidth > 300);
                    return el ? el.firstElementChild : null;
                }),
                footerInner: dumpChildren('[data-framer-name="Footer"] > *')
            };
        }""")

        with open(r"d:\margin-framer-template\mobile_inners.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        print("Saved to mobile_inners.json")
        browser.close()

if __name__ == "__main__":
    inspect_mobile_inners()
