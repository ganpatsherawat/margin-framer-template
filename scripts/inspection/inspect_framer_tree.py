import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_framer_tree():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        # Inspect children of the main desktop container
        structure = page.evaluate("""() => {
            const desktop = document.querySelector('[data-framer-name="Desktop"]');
            if (!desktop) return { error: "Desktop container not found" };

            // Find direct children
            const children = Array.from(desktop.children).map((child, idx) => {
                const rect = child.getBoundingClientRect();
                const style = window.getComputedStyle(child);
                return {
                    index: idx,
                    tag: child.tagName,
                    framerName: child.getAttribute('data-framer-name') || '',
                    id: child.id,
                    className: child.className.slice(0, 30),
                    top: rect.top + window.scrollY,
                    height: rect.height,
                    width: rect.width,
                    text: (child.innerText || '').slice(0, 60).replace(/\\n/g, ' '),
                    display: style.display,
                    position: style.position,
                    gap: style.gap,
                    padding: style.padding,
                    margin: style.margin,
                    backgroundColor: style.backgroundColor
                };
            });

            return {
                desktopWidth: desktop.getBoundingClientRect().width,
                desktopHeight: desktop.getBoundingClientRect().height,
                children
            };
        }""")

        print(json.dumps(structure, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_framer_tree()
