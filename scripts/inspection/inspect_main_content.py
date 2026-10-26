import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_main_content():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        sections = page.evaluate("""() => {
            const wrapper = document.querySelector('.framer-LOxyv') || document.querySelector('body > div');
            let target = wrapper;
            while (target && target.children.length === 1 && target.firstElementChild.tagName === 'DIV') {
                target = target.firstElementChild;
            }

            const mainSection = target.children[2];
            // If mainSection has children, list them
            let container = mainSection;
            while (container && container.children.length === 1) {
                container = container.firstElementChild;
            }

            return Array.from(container.children).map((c, i) => {
                const r = c.getBoundingClientRect();
                const s = window.getComputedStyle(c);
                return {
                    i,
                    tag: c.tagName,
                    framerName: c.getAttribute('data-framer-name'),
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    margin: s.margin,
                    gap: s.gap,
                    maxWidth: s.maxWidth,
                    text: (c.innerText || '').slice(0, 70).replace(/\\n/g, ' ')
                };
            });
        }""")

        with open(r"d:\margin-framer-template\framer_main_sections.json", "w", encoding="utf-8") as f:
            json.dump(sections, f, indent=2)

        for s in sections:
            print(f"[{s['i']}] top={s['top']} h={s['height']} w={s['width']} pad={s['padding']} gap={s['gap']} name='{s['framerName']}' text='{s['text']}'")

        browser.close()

if __name__ == "__main__":
    inspect_main_content()
