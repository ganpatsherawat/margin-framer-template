import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_testimonial():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            const section = Array.from(document.querySelectorAll('*')).find(e => e.getAttribute('data-framer-name') === 'Photo quote');
            if (!section) return { error: "Photo quote not found" };

            const r = section.getBoundingClientRect();
            const s = window.getComputedStyle(section);

            // Find image and quote elements
            const img = section.querySelector('img');
            const ir = img ? img.getBoundingClientRect() : {};
            const is = img ? window.getComputedStyle(img) : {};

            const quote = Array.from(section.querySelectorAll('*')).find(e => e.innerText && e.innerText.includes('Nora talked us out') && e.children.length === 0);
            const qr = quote ? quote.getBoundingClientRect() : {};
            const qs = quote ? window.getComputedStyle(quote) : {};

            return {
                section: {
                    top: Math.round(r.top + window.scrollY),
                    height: Math.round(r.height),
                    width: Math.round(r.width),
                    padding: s.padding,
                    backgroundColor: s.backgroundColor
                },
                image: {
                    top: Math.round(ir.top + window.scrollY),
                    left: Math.round(ir.left),
                    width: Math.round(ir.width),
                    height: Math.round(ir.height),
                    borderRadius: is.borderRadius
                },
                quote: {
                    top: Math.round(qr.top + window.scrollY),
                    left: Math.round(qr.left),
                    width: Math.round(qr.width),
                    height: Math.round(qr.height),
                    fontSize: qs.fontSize,
                    lineHeight: qs.lineHeight,
                    fontFamily: qs.fontFamily
                }
            };
        }""")

        print(json.dumps(details, indent=2))
        browser.close()

if __name__ == "__main__":
    inspect_testimonial()
