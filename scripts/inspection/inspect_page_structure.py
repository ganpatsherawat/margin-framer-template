import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_page_structure():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        structure = page.evaluate("""() => {
            // Find the main wrapper div inside body
            // Usually #main or div with id='overlay' or framer root
            const root = document.querySelector('#main') || document.body.firstElementChild;
            
            // Find all elements directly descending from main container
            function findMajorBlocks(el) {
                // Find all direct children or elements with height > 100
                const all = Array.from(document.querySelectorAll('*'));
                // Filter elements whose direct parent is the main page container
                // Or look at children of the main page stack
                const pageContainer = all.find(e => {
                    const r = e.getBoundingClientRect();
                    return r.width >= 1200 && r.height > 4000;
                });

                if (!pageContainer) return { error: "Page container not found" };

                const blocks = Array.from(pageContainer.children).map((c, i) => {
                    const rect = c.getBoundingClientRect();
                    const s = window.getComputedStyle(c);
                    return {
                        i,
                        tag: c.tagName,
                        framerName: c.getAttribute('data-framer-name'),
                        top: Math.round(rect.top + window.scrollY),
                        height: Math.round(rect.height),
                        width: Math.round(rect.width),
                        display: s.display,
                        flexDirection: s.flexDirection,
                        padding: s.padding,
                        margin: s.margin,
                        gap: s.gap,
                        maxWidth: s.maxWidth,
                        text: (c.innerText || '').slice(0, 80).replace(/\\n/g, ' ')
                    };
                });

                return {
                    containerTag: pageContainer.tagName,
                    containerClass: pageContainer.className,
                    containerWidth: Math.round(pageContainer.getBoundingClientRect().width),
                    containerHeight: Math.round(pageContainer.getBoundingClientRect().height),
                    blocks
                };
            }

            return findMajorBlocks();
        }""")

        print(json.dumps(structure, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_page_structure()
