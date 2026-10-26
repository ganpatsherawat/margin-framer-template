import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_sections_both():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for mode, width, height in [("desktop", 1440, 900), ("mobile", 390, 844)]:
            print(f"\n=================== {mode.upper()} ({width}x{height}) ===================")
            
            # 1. Ref page
            page_ref = browser.new_page(viewport={"width": width, "height": height})
            page_ref.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
            page_ref.wait_for_timeout(1500)
            
            ref_sections = page_ref.evaluate("""() => {
                const results = [];
                // Find main direct children or sections
                const root = document.querySelector('[data-framer-name="Desktop"], [data-framer-name="Phone"], main, body > div');
                const elements = Array.from(document.querySelectorAll('section, header, footer, [data-framer-name]'));
                
                // Let's get bounding rect of key elements by text or tag
                const keys = [
                    { name: "header", sel: "header, [data-framer-name*='Navigation'], [data-framer-name*='Nav']" },
                    { name: "hero", sel: "h1" },
                    { name: "decision_record", text: "The not-now list" },
                    { name: "ticker", text: "fernhill" },
                    { name: "services", text: "What we’re hired for" },
                    { name: "featured_case", text: "+41%" },
                    { name: "work", text: "Selected work" },
                    { name: "testimonial", text: "Nora talked us out" },
                    { name: "pre_footer_cta", text: "Tell us what’s stuck." },
                    { name: "footer", sel: "footer, [data-framer-name*='Footer']" }
                ];

                return keys.map(k => {
                    let el = null;
                    if (k.text) {
                        const all = Array.from(document.querySelectorAll('*'));
                        el = all.find(e => e.innerText && e.innerText.includes(k.text) && e.children.length < 5);
                        if (el) {
                            // Find section or parent container
                            while (el.parentElement && el.parentElement !== document.body && el.offsetHeight < 100) {
                                el = el.parentElement;
                            }
                        }
                    } else if (k.sel) {
                        el = document.querySelector(k.sel);
                    }
                    if (!el) return { name: k.name, found: false };
                    const rect = el.getBoundingClientRect();
                    const style = window.getComputedStyle(el);
                    return {
                        name: k.name,
                        found: true,
                        top: rect.top + window.scrollY,
                        height: rect.height,
                        width: rect.width,
                        padding: style.padding,
                        margin: style.margin,
                        fontSize: style.fontSize,
                        lineHeight: style.lineHeight
                    };
                });
            }""")
            page_ref.close()

            # 2. Duplicate page
            page_dup = browser.new_page(viewport={"width": width, "height": height})
            page_dup.goto("http://localhost:4321/", wait_until="networkidle")
            page_dup.wait_for_timeout(1500)

            dup_sections = page_dup.evaluate("""() => {
                const keys = [
                    { name: "header", sel: "header" },
                    { name: "hero", sel: ".hero-section" },
                    { name: "decision_record", sel: ".decision-card-container" },
                    { name: "ticker", sel: ".ticker-section" },
                    { name: "services", sel: ".services-section" },
                    { name: "featured_case", sel: ".featured-callout" },
                    { name: "work", sel: "#work" },
                    { name: "testimonial", sel: ".testimonial-section" },
                    { name: "pre_footer_cta", sel: ".pre-footer-cta" },
                    { name: "footer", sel: ".site-footer" }
                ];

                return keys.map(k => {
                    const el = document.querySelector(k.sel);
                    if (!el) return { name: k.name, found: false };
                    const rect = el.getBoundingClientRect();
                    const style = window.getComputedStyle(el);
                    return {
                        name: k.name,
                        found: true,
                        top: rect.top + window.scrollY,
                        height: rect.height,
                        width: rect.width,
                        padding: style.padding,
                        margin: style.margin
                    };
                });
            }""")
            page_dup.close()

            print(f"{'SECTION':<20} | {'REF TOP':<10} | {'DUP TOP':<10} | {'REF H':<10} | {'DUP H':<10} | {'DIFF H'}")
            print("-" * 75)
            for r, d in zip(ref_sections, dup_sections):
                r_top = f"{round(r.get('top', 0))}px" if r.get('found') else "N/A"
                d_top = f"{round(d.get('top', 0))}px" if d.get('found') else "N/A"
                r_h = f"{round(r.get('height', 0))}px" if r.get('found') else "N/A"
                d_h = f"{round(d.get('height', 0))}px" if d.get('found') else "N/A"
                diff = round(d.get('height', 0) - r.get('height', 0)) if (r.get('found') and d.get('found')) else "N/A"
                print(f"{r['name']:<20} | {r_top:<10} | {d_top:<10} | {r_h:<10} | {d_h:<10} | {diff}")

        browser.close()

if __name__ == "__main__":
    inspect_sections_both()
