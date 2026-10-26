import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def compare_hero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page_ref = browser.new_page(viewport={"width": 1440, "height": 900})
        page_ref.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page_ref.wait_for_timeout(2000)

        page_dup = browser.new_page(viewport={"width": 1440, "height": 900})
        page_dup.goto("http://localhost:4321/", wait_until="networkidle")
        page_dup.wait_for_timeout(2000)

        ref_h1 = page_ref.evaluate("""() => {
            const h1 = document.querySelector('h1');
            const r = h1.getBoundingClientRect();
            const s = window.getComputedStyle(h1);
            const p = h1.parentElement;
            const pr = p.getBoundingClientRect();
            const ps = window.getComputedStyle(p);
            return {
                h1: { top: Math.round(r.top + window.scrollY), height: Math.round(r.height), fontSize: s.fontSize, lineHeight: s.lineHeight, mb: s.marginBottom },
                copy: { top: Math.round(pr.top + window.scrollY), height: Math.round(pr.height), gap: ps.gap, padding: ps.padding }
            };
        }""")

        dup_h1 = page_dup.evaluate("""() => {
            const h1 = document.querySelector('h1');
            const r = h1.getBoundingClientRect();
            const s = window.getComputedStyle(h1);
            const p = h1.parentElement;
            const pr = p.getBoundingClientRect();
            const ps = window.getComputedStyle(p);
            return {
                h1: { top: Math.round(r.top + window.scrollY), height: Math.round(r.height), fontSize: s.fontSize, lineHeight: s.lineHeight, mb: s.marginBottom },
                copy: { top: Math.round(pr.top + window.scrollY), height: Math.round(pr.height), gap: ps.gap, padding: ps.padding }
            };
        }""")

        print("REF H1/Copy:", json.dumps(ref_h1, indent=2))
        print("DUP H1/Copy:", json.dumps(dup_h1, indent=2))

        # Showcase
        ref_show = page_ref.evaluate("""() => {
            const el = document.querySelector('[data-framer-name="Showcase"]');
            const r = el.getBoundingClientRect();
            return { top: Math.round(r.top + window.scrollY), height: Math.round(r.height), width: Math.round(r.width) };
        }""")

        dup_show = page_dup.evaluate("""() => {
            const el = document.querySelector('.hero-showcase');
            const r = el ? el.getBoundingClientRect() : {};
            return { top: Math.round((r.top || 0) + window.scrollY), height: Math.round(r.height || 0), width: Math.round(r.width || 0) };
        }""")

        print("REF Showcase:", ref_show)
        print("DUP Showcase:", dup_show)

        browser.close()

if __name__ == "__main__":
    compare_hero()
