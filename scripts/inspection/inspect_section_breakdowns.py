import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_breakdowns():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        details = page.evaluate("""() => {
            function dumpChildren(el) {
                if (!el) return null;
                return Array.from(el.children).map(c => {
                    const r = c.getBoundingClientRect();
                    const s = window.getComputedStyle(c);
                    return {
                        tag: c.tagName,
                        name: c.getAttribute('data-framer-name'),
                        top: Math.round(r.top + window.scrollY),
                        height: Math.round(r.height),
                        width: Math.round(r.width),
                        padding: s.padding,
                        margin: s.margin,
                        gap: s.gap,
                        fontSize: s.fontSize,
                        lineHeight: s.lineHeight,
                        text: (c.innerText || '').slice(0, 50).replace(/\\n/g, ' ')
                    };
                });
            }

            const mainChildren = Array.from(document.querySelectorAll('.framer-LOxyv > div > div > *') || []);
            // find by text
            const servicesEl = document.querySelector('[data-framer-name="Services"]');
            const bigNumEl = document.querySelector('[data-framer-name="Big number"]');
            const workEl = document.querySelector('[data-framer-name="Selected work"]');
            const ctaEl = Array.from(document.querySelectorAll('*')).find(el => el.innerText && el.innerText.startsWith('BOOKING FROM JANUARY 2027') && el.offsetWidth > 1000);
            const footerEl = document.querySelector('[data-framer-name="Footer"]');

            return {
                services: {
                    rect: servicesEl ? { top: Math.round(servicesEl.getBoundingClientRect().top + window.scrollY), height: Math.round(servicesEl.getBoundingClientRect().height) } : null,
                    pad: servicesEl ? window.getComputedStyle(servicesEl).padding : null,
                    children: dumpChildren(servicesEl)
                },
                bigNum: {
                    rect: bigNumEl ? { top: Math.round(bigNumEl.getBoundingClientRect().top + window.scrollY), height: Math.round(bigNumEl.getBoundingClientRect().height) } : null,
                    pad: bigNumEl ? window.getComputedStyle(bigNumEl).padding : null,
                    children: dumpChildren(bigNumEl)
                },
                work: {
                    rect: workEl ? { top: Math.round(workEl.getBoundingClientRect().top + window.scrollY), height: Math.round(workEl.getBoundingClientRect().height) } : null,
                    pad: workEl ? window.getComputedStyle(workEl).padding : null,
                    children: dumpChildren(workEl)
                },
                cta: {
                    rect: ctaEl ? { top: Math.round(ctaEl.getBoundingClientRect().top + window.scrollY), height: Math.round(ctaEl.getBoundingClientRect().height) } : null,
                    pad: ctaEl ? window.getComputedStyle(ctaEl).padding : null,
                    children: dumpChildren(ctaEl)
                },
                footer: {
                    rect: footerEl ? { top: Math.round(footerEl.getBoundingClientRect().top + window.scrollY), height: Math.round(footerEl.getBoundingClientRect().height) } : null,
                    pad: footerEl ? window.getComputedStyle(footerEl).padding : null,
                    children: dumpChildren(footerEl)
                }
            };
        }""")

        with open(r"d:\margin-framer-template\breakdowns.json", "w", encoding="utf-8") as f:
            json.dump(details, f, indent=2)

        print("Breakdowns saved to breakdowns.json")
        browser.close()

if __name__ == "__main__":
    inspect_breakdowns()
