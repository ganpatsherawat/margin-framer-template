import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_prefooter():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            const h2 = Array.from(document.querySelectorAll('*')).find(e => e.innerText && e.innerText.trim() === 'Tell us what’s stuck.');
            if (!h2) return { error: "Heading not found" };

            let container = h2;
            while (container.parentElement && container.parentElement !== document.body && container.offsetWidth < 1200) {
                container = container.parentElement;
            }

            const cr = container.getBoundingClientRect();
            const cs = window.getComputedStyle(container);

            const hr = h2.getBoundingClientRect();
            const hs = window.getComputedStyle(h2);

            return {
                container: {
                    tag: container.tagName,
                    framerName: container.getAttribute('data-framer-name'),
                    top: Math.round(cr.top + window.scrollY),
                    height: Math.round(cr.height),
                    width: Math.round(cr.width),
                    padding: cs.padding,
                    margin: cs.margin,
                    backgroundColor: cs.backgroundColor
                },
                heading: {
                    top: Math.round(hr.top + window.scrollY),
                    left: Math.round(hr.left),
                    width: Math.round(hr.width),
                    height: Math.round(hr.height),
                    fontSize: hs.fontSize,
                    lineHeight: hs.lineHeight,
                    color: hs.color,
                    fontFamily: hs.fontFamily
                },
                html: container.outerHTML.slice(0, 1000)
            };
        }""")

        print(json.dumps(details, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_prefooter()
