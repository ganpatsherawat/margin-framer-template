import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_cta():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            const section = Array.from(document.querySelectorAll('*')).find(e => e.getAttribute('data-framer-name') === 'Call to action');
            if (!section) return { error: "Call to action not found" };

            const r = section.getBoundingClientRect();
            const s = window.getComputedStyle(section);

            // Find heading and button
            const heading = section.querySelector('h2');
            const hs = heading ? window.getComputedStyle(heading) : {};
            const hr = heading ? heading.getBoundingClientRect() : {};

            const btn = section.querySelector('a[href="/contact"]');
            const bs = btn ? window.getComputedStyle(btn) : {};
            const br = btn ? btn.getBoundingClientRect() : {};

            return {
                section: {
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    backgroundColor: s.backgroundColor
                },
                heading: {
                    top: Math.round(hr.top + window.scrollY),
                    left: Math.round(hr.left),
                    width: Math.round(hr.width),
                    height: Math.round(hr.height),
                    fontSize: hs.fontSize,
                    lineHeight: hs.lineHeight,
                    color: hs.color
                },
                button: {
                    top: Math.round(br.top + window.scrollY),
                    left: Math.round(br.left),
                    width: Math.round(br.width),
                    height: Math.round(br.height),
                    backgroundColor: bs.backgroundColor,
                    borderRadius: bs.borderRadius,
                    padding: bs.padding
                }
            };
        }""")

        print(json.dumps(details, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_cta()
