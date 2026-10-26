import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def compare_fastly_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page_ref = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
        page_ref.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page_ref.wait_for_timeout(2000)

        page_live = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
        page_live.goto("https://hoox-advisory.global.ssl.fastly.net/", wait_until="networkidle")
        page_live.wait_for_timeout(2000)

        sections = [
            ("Hero", 'document.querySelector(\'[data-framer-name="Hero"]\')', 'document.querySelector(\'.hero-section\')'),
            ("Clients (in Hero)", 'document.querySelector(\'[data-framer-name="Clients"]\')', 'document.querySelector(\'.hero-clients-marquee\')'),
            ("Services", 'document.querySelector(\'[data-framer-name="Services"]\')', 'document.querySelector(\'.services-section\')'),
            ("Big number", 'document.querySelector(\'[data-framer-name="Big number"]\')', 'document.querySelector(\'.featured-case-section\')'),
            ("Selected work", 'document.querySelector(\'[data-framer-name="Selected work"]\')', 'document.querySelector(\'.selected-work-section\')'),
            ("Photo quote", 'document.querySelector(\'[data-framer-name="Photo quote"]\')', 'document.querySelector(\'.testimonial-hero-section\')'),
            ("Call to action", 'Array.from(document.querySelectorAll(\'*\')).find(el => el.innerText && el.innerText.startsWith(\'BOOKING FROM JANUARY 2027\') && el.offsetWidth > 300)', 'document.querySelector(\'.pre-footer-cta-section\')'),
            ("Footer", 'document.querySelector(\'[data-framer-name="Footer"]\')', 'document.querySelector(\'.site-footer\')')
        ]

        print("=== FASTLY LIVE MOBILE SECTION COMPARISON ===")
        print(f"{'SECTION':<20} | {'REF TOP':<8} | {'LIVE TOP':<8} | {'REF H':<8} | {'LIVE H':<8} | {'DIFF H':<8} | {'DIFF TOP'}")
        print("-" * 84)

        for name, ref_expr, live_expr in sections:
            ref_info = page_ref.evaluate(f"""() => {{
                const el = {ref_expr};
                if (!el) return {{ found: false }};
                const r = el.getBoundingClientRect();
                return {{ found: true, top: Math.round(r.top + window.scrollY), height: Math.round(r.height) }};
            }}""")

            live_info = page_live.evaluate(f"""() => {{
                const el = {live_expr};
                if (!el) return {{ found: false }};
                const r = el.getBoundingClientRect();
                return {{ found: true, top: Math.round(r.top + window.scrollY), height: Math.round(r.height) }};
            }}""")

            if ref_info['found'] and live_info['found']:
                diff_h = live_info['height'] - ref_info['height']
                diff_top = live_info['top'] - ref_info['top']
                print(f"{name:<20} | {ref_info['top']:<8} | {live_info['top']:<8} | {ref_info['height']:<8} | {live_info['height']:<8} | {diff_h:<8} | {diff_top}")

        browser.close()

if __name__ == "__main__":
    compare_fastly_mobile()
