import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_footer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        data = page.evaluate("""() => {
            const f = document.querySelector('[data-framer-name="Footer"]');
            const fr = f.getBoundingClientRect();
            const fs = window.getComputedStyle(f);

            function getTree(el) {
                if (!el) return null;
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                return {
                    name: el.getAttribute('data-framer-name'),
                    tag: el.tagName,
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    pad: s.padding,
                    margin: s.margin,
                    gap: s.gap,
                    display: s.display,
                    justifyContent: s.justifyContent,
                    alignItems: s.alignItems,
                    flexDirection: s.flexDirection,
                    text: (el.innerText || '').slice(0, 30).replace(/\\n/g, ' '),
                    children: Array.from(el.children).map(getTree)
                };
            }

            return {
                footer: {
                    top: Math.round(fr.top + window.scrollY),
                    height: Math.round(fr.height),
                    pad: fs.padding,
                    display: fs.display,
                    justifyContent: fs.justifyContent
                },
                inner: getTree(f.firstElementChild)
            };
        }""")

        print(json.dumps(data, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_footer()
