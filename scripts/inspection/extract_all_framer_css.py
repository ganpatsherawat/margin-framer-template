import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def get_style(page, selector, desc):
    return page.evaluate("""([sel, description]) => {
        const el = document.querySelector(sel);
        if (!el) return { desc: description, found: false };
        const s = window.getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return {
            desc: description,
            found: true,
            tagName: el.tagName,
            rect: { top: Math.round(r.top + window.scrollY), left: Math.round(r.left), width: Math.round(r.width), height: Math.round(r.height) },
            fontFamily: s.fontFamily,
            fontSize: s.fontSize,
            fontWeight: s.fontWeight,
            lineHeight: s.lineHeight,
            letterSpacing: s.letterSpacing,
            color: s.color,
            backgroundColor: s.backgroundColor,
            borderRadius: s.borderRadius,
            padding: s.padding,
            margin: s.margin,
            border: s.border,
            boxShadow: s.boxShadow,
            gap: s.gap
        };
    }""", [selector, desc])

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        selectors = [
            ('header, nav, [data-framer-name="Header band"]', 'Header Band'),
            ('[data-framer-name="Desktop"]', 'Desktop Nav Container'),
            ('a[href="/"]', 'Logo Link'),
            ('[data-framer-name="Links"] a', 'Nav Link'),
            ('a[href="/contact"]', 'Nav CTA Button'),
            ('h1', 'Hero Headline'),
            ('img[alt*="meeting room"]', 'Hero Image'),
            ('img[alt*="whiteboard"]', 'Decision Record Image'),
            ('[data-framer-name*="Clients"], [data-framer-name*="Ticker"]', 'Ticker Container'),
            ('[data-framer-name*="Services"]', 'Services Container'),
            ('[data-framer-name*="Big number"]', 'Featured Case Container'),
            ('[data-framer-name*="Selected work"]', 'Selected Work Container'),
            ('[data-framer-name*="Photo quote"]', 'Testimonial Container'),
            ('[data-framer-name*="Call to action"]', 'Pre-footer CTA Container'),
            ('[data-framer-name*="Footer"]', 'Footer Container')
        ]

        results = []
        for sel, desc in selectors:
            res = get_style(page, sel, desc)
            results.append(res)
            print(f"=== {desc} ===")
            print(json.dumps(res, indent=2))

        with open(r"d:\margin-framer-template\all_framer_computed_styles.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

        browser.close()

if __name__ == "__main__":
    run()
