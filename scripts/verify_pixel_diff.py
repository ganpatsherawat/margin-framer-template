"""
Automated Section Height & Top Position Verification Tool.
Compares either local (localhost:4321) or live Fastly URL against the reference Framer site.
"""

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import argparse
from playwright.sync_api import sync_playwright

SECTIONS_DESKTOP = [
    ("Hero", 'document.querySelector(\'[data-framer-name="Hero"]\')', 'document.querySelector(\'.hero-section\')'),
    ("Clients (in Hero)", 'document.querySelector(\'[data-framer-name="Clients"]\')', 'document.querySelector(\'.hero-clients-marquee\')'),
    ("Services", 'document.querySelector(\'[data-framer-name="Services"]\')', 'document.querySelector(\'.services-section\')'),
    ("Big number", 'document.querySelector(\'[data-framer-name="Big number"]\')', 'document.querySelector(\'.featured-case-section\')'),
    ("Selected work", 'document.querySelector(\'[data-framer-name="Selected work"]\')', 'document.querySelector(\'.selected-work-section\')'),
    ("Photo quote", 'document.querySelector(\'[data-framer-name="Photo quote"]\')', 'document.querySelector(\'.testimonial-hero-section\')'),
    ("Call to action", 'Array.from(document.querySelectorAll(\'*\')).find(el => el.innerText && el.innerText.startsWith(\'BOOKING FROM JANUARY 2027\') && el.offsetWidth > 1000)', 'document.querySelector(\'.pre-footer-cta-section\')'),
    ("Footer", 'document.querySelector(\'[data-framer-name="Footer"]\')', 'document.querySelector(\'.site-footer\')')
]

SECTIONS_MOBILE = [
    ("Hero", 'document.querySelector(\'[data-framer-name="Hero"]\')', 'document.querySelector(\'.hero-section\')'),
    ("Clients (in Hero)", 'document.querySelector(\'[data-framer-name="Clients"]\')', 'document.querySelector(\'.hero-clients-marquee\')'),
    ("Services", 'document.querySelector(\'[data-framer-name="Services"]\')', 'document.querySelector(\'.services-section\')'),
    ("Big number", 'document.querySelector(\'[data-framer-name="Big number"]\')', 'document.querySelector(\'.featured-case-section\')'),
    ("Selected work", 'document.querySelector(\'[data-framer-name="Selected work"]\')', 'document.querySelector(\'.selected-work-section\')'),
    ("Photo quote", 'document.querySelector(\'[data-framer-name="Photo quote"]\')', 'document.querySelector(\'.testimonial-hero-section\')'),
    ("Call to action", 'Array.from(document.querySelectorAll(\'*\')).find(el => el.innerText && el.innerText.startsWith(\'BOOKING FROM JANUARY 2027\') && el.offsetWidth > 300)', 'document.querySelector(\'.pre-footer-cta-section\')'),
    ("Footer", 'document.querySelector(\'[data-framer-name="Footer"]\')', 'document.querySelector(\'.site-footer\')')
]

def verify(target_url, mode="both"):
    ref_url = "https://essential-time-088020.framer.app/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        if mode in ("desktop", "both"):
            print(f"\n================ DESKTOP (1440x900) VERIFICATION: {target_url} ================")
            print(f"{'SECTION':<20} | {'REF TOP':<8} | {'TARGET TOP':<10} | {'REF H':<8} | {'TARGET H':<8} | {'DIFF H':<8} | {'DIFF TOP'}")
            print("-" * 88)

            page_ref = browser.new_page(viewport={"width": 1440, "height": 900})
            page_ref.goto(ref_url, wait_until="load", timeout=60000)
            page_ref.wait_for_timeout(2000)

            page_tar = browser.new_page(viewport={"width": 1440, "height": 900})
            page_tar.goto(target_url, wait_until="load", timeout=60000)
            page_tar.wait_for_timeout(2000)

            for name, ref_expr, tar_expr in SECTIONS_DESKTOP:
                r_info = page_ref.evaluate(f"() => {{ const el = {ref_expr}; return el ? {{ top: Math.round(el.getBoundingClientRect().top + window.scrollY), height: Math.round(el.getBoundingClientRect().height) }} : null; }}")
                t_info = page_tar.evaluate(f"() => {{ const el = {tar_expr}; return el ? {{ top: Math.round(el.getBoundingClientRect().top + window.scrollY), height: Math.round(el.getBoundingClientRect().height) }} : null; }}")
                if r_info and t_info:
                    dh = t_info['height'] - r_info['height']
                    dt = t_info['top'] - r_info['top']
                    print(f"{name:<20} | {r_info['top']:<8} | {t_info['top']:<10} | {r_info['height']:<8} | {t_info['height']:<8} | {dh:<8} | {dt}")

            page_ref.close()
            page_tar.close()

        if mode in ("mobile", "both"):
            print(f"\n================ MOBILE (390x844) VERIFICATION: {target_url} ================")
            print(f"{'SECTION':<20} | {'REF TOP':<8} | {'TARGET TOP':<10} | {'REF H':<8} | {'TARGET H':<8} | {'DIFF H':<8} | {'DIFF TOP'}")
            print("-" * 88)

            page_ref = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
            page_ref.goto(ref_url, wait_until="load", timeout=60000)
            page_ref.wait_for_timeout(2000)

            page_tar = browser.new_page(viewport={"width": 390, "height": 844}, is_mobile=True)
            page_tar.goto(target_url, wait_until="load", timeout=60000)
            page_tar.wait_for_timeout(2000)

            for name, ref_expr, tar_expr in SECTIONS_MOBILE:
                r_info = page_ref.evaluate(f"() => {{ const el = {ref_expr}; return el ? {{ top: Math.round(el.getBoundingClientRect().top + window.scrollY), height: Math.round(el.getBoundingClientRect().height) }} : null; }}")
                t_info = page_tar.evaluate(f"() => {{ const el = {tar_expr}; return el ? {{ top: Math.round(el.getBoundingClientRect().top + window.scrollY), height: Math.round(el.getBoundingClientRect().height) }} : null; }}")
                if r_info and t_info:
                    dh = t_info['height'] - r_info['height']
                    dt = t_info['top'] - r_info['top']
                    print(f"{name:<20} | {r_info['top']:<8} | {t_info['top']:<10} | {r_info['height']:<8} | {t_info['height']:<8} | {dh:<8} | {dt}")

            page_ref.close()
            page_tar.close()

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify section pixel fidelity against Framer reference")
    parser.add_argument("url", nargs="?", default="https://hoox-advisory.global.ssl.fastly.net/", help="URL to verify (default: live Fastly production)")
    parser.add_argument("--mode", choices=["desktop", "mobile", "both"], default="both", help="Viewport mode to test")
    args = parser.parse_args()

    verify(args.url, mode=args.mode)
