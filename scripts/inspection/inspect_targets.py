import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
import json
from playwright.sync_api import sync_playwright

def inspect_all_visible_blocks():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        blocks = page.evaluate("""() => {
            const results = [];
            // Walk all elements and find significant visible cards/sections
            const elements = Array.from(document.querySelectorAll('*'));
            
            // Search by text phrases
            const targets = [
                { id: "hero_h1", text: "We help growing companies" },
                { id: "hero_sub", text: "Two partners, four clients at a time" },
                { id: "hero_cta", text: "Thirty minutes with a partner. Free." },
                { id: "hero_btn", text: "Book an intro call" },
                { id: "decision_header", text: "DECISION RECORD · Q1 2027" },
                { id: "decision_title", text: "The not-now list" },
                { id: "decision_stop1", text: "Enter the German market" },
                { id: "decision_fund1", text: "Rebuild the ICP around retention" },
                { id: "ticker", text: "fernhill" },
                { id: "services_heading", text: "What we’re hired for" },
                { id: "services_row1", text: "Positioning" },
                { id: "services_row2", text: "Go-to-market" },
                { id: "services_row3", text: "Advisory" },
                { id: "featured_case_metric", text: "+41%" },
                { id: "featured_case_text", text: "more qualified pipeline" },
                { id: "work_heading", text: "Selected work" },
                { id: "work_case1", text: "FREIGHT SOFTWARE" },
                { id: "work_case2", text: "CLINIC SOFTWARE" },
                { id: "work_case3", text: "ARCHITECTURE" },
                { id: "quote", text: "Nora talked us out of a rebrand" },
                { id: "quote_author", text: "Elena Sousa" },
                { id: "prefooter_heading", text: "Tell us what’s stuck." },
                { id: "prefooter_cta", text: "Thirty minutes with a partner. Free, and useful either way." }
            ];

            return targets.map(t => {
                const el = elements.find(e => e.innerText && e.innerText.trim().startsWith(t.text) && e.children.length === 0) ||
                           elements.find(e => e.innerText && e.innerText.trim().includes(t.text) && e.children.length <= 2);
                if (!el) return { id: t.id, found: false };
                const r = el.getBoundingClientRect();
                const s = window.getComputedStyle(el);
                
                // Also get direct card or container
                let container = el;
                while (container.parentElement && container.parentElement !== document.body && container.offsetHeight < 150) {
                    container = container.parentElement;
                }
                const cr = container.getBoundingClientRect();
                const cs = window.getComputedStyle(container);

                return {
                    id: t.id,
                    found: true,
                    text: el.innerText.trim().slice(0, 50).replace(/\\n/g, ' '),
                    rect: { top: Math.round(r.top + window.scrollY), left: Math.round(r.left), width: Math.round(r.width), height: Math.round(r.height) },
                    style: {
                        fontFamily: s.fontFamily,
                        fontSize: s.fontSize,
                        fontWeight: s.fontWeight,
                        lineHeight: s.lineHeight,
                        color: s.color,
                        textAlign: s.textAlign
                    },
                    container: {
                        tag: container.tagName,
                        rect: { top: Math.round(cr.top + window.scrollY), left: Math.round(cr.left), width: Math.round(cr.width), height: Math.round(cr.height) },
                        backgroundColor: cs.backgroundColor,
                        borderRadius: cs.borderRadius,
                        padding: cs.padding,
                        margin: cs.margin
                    }
                };
            });
        }""")

        with open(r"d:\margin-framer-template\all_targets.json", "w", encoding="utf-8") as f:
            json.dump(blocks, f, indent=2)

        for b in blocks:
            if b.get("found"):
                r = b["rect"]
                s = b["style"]
                print(f"{b['id']:<22} | top={r['top']:<5} left={r['left']:<5} w={r['width']:<5} h={r['height']:<5} | fs={s['fontSize']:<6} lh={s['lineHeight']:<7} align={s['textAlign']}")

        browser.close()

if __name__ == "__main__":
    inspect_all_visible_blocks()
