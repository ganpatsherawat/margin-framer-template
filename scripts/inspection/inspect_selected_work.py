import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_selected_work():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            const section = Array.from(document.querySelectorAll('*')).find(e => e.getAttribute('data-framer-name') === 'Selected work');
            if (!section) return { error: "Selected work not found" };

            const r = section.getBoundingClientRect();
            const s = window.getComputedStyle(section);

            // Find all children or cards/rows
            const rows = Array.from(section.querySelectorAll('a, [data-framer-name*="Row"], [data-framer-name*="Item"], [data-framer-name*="Card"]')).map(el => {
                const er = el.getBoundingClientRect();
                const es = window.getComputedStyle(el);
                return {
                    tag: el.tagName,
                    framerName: el.getAttribute('data-framer-name'),
                    top: Math.round(er.top + window.scrollY),
                    left: Math.round(er.left),
                    width: Math.round(er.width),
                    height: Math.round(er.height),
                    text: (el.innerText || '').slice(0, 80).replace(/\\n/g, ' '),
                    display: es.display,
                    borderBottom: es.borderBottom
                };
            });

            return {
                section: {
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding
                },
                rows: rows.filter(x => x.height > 40 && x.width > 500)
            };
        }""")

        print(json.dumps(details, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_selected_work()
