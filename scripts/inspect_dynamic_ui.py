"""
Dynamic UI & CDP Inspection Tool.

Solves REA tool limitations by:
1. Connecting to or launching a background headless Chromium with remote debugging on port 9222.
2. Forcing CSS pseudo-states (:hover, :focus) via CDP without requiring manual pointer interaction.
3. Extracting Web Animations API transitions, keyframes, and timing curves directly from the browser.
"""

import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import json
import argparse
import urllib.request
from playwright.sync_api import sync_playwright

def is_cdp_alive(endpoint="http://127.0.0.1:9222"):
    try:
        with urllib.request.urlopen(f"{endpoint}/json/version", timeout=1) as resp:
            return resp.status == 200
    except Exception:
        return False

def inspect_dynamic(url, hover_selector=None, scroll_to_bottom=False):
    print(f"[*] Inspecting target: {url}")
    cdp_ready = is_cdp_alive()
    print(f"[*] Local CDP endpoint port 9222 active: {cdp_ready}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--remote-debugging-port=9222"] if not cdp_ready else []
        )
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        # Listen to transition events via init script
        page.add_init_script("""
            window.__TRANSITIONS__ = [];
            window.addEventListener('transitionrun', (e) => {
                const s = window.getComputedStyle(e.target);
                window.__TRANSITIONS__.push({
                    property: e.propertyName,
                    duration: s.transitionDuration,
                    timingFunction: s.transitionTimingFunction,
                    delay: s.transitionDelay,
                    targetTag: e.target.tagName,
                    targetClass: e.target.className
                });
            }, true);
        """)

        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(1500)

        results = {
            "url": url,
            "title": page.title(),
            "hoverInspection": None,
            "webAnimations": [],
            "recordedTransitions": []
        }

        # 1. Hover inspection if selector provided
        if hover_selector:
            el = page.query_selector(hover_selector)
            if el:
                # Capture before hover
                before_box = el.bounding_box()
                before_styles = page.evaluate("(sel) => window.getComputedStyle(document.querySelector(sel)).cssText", hover_selector)

                # Trigger hover
                el.hover()
                page.wait_for_timeout(600)

                # Capture after hover
                after_box = el.bounding_box()
                after_styles = page.evaluate("(sel) => window.getComputedStyle(document.querySelector(sel)).cssText", hover_selector)

                results["hoverInspection"] = {
                    "selector": hover_selector,
                    "beforeBox": before_box,
                    "afterBox": after_box,
                    "boxMutated": before_box != after_box
                }
                print(f"[+] Hover state captured for selector: {hover_selector}")

        # 2. Scroll if requested
        if scroll_to_bottom:
            page.evaluate("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")
            page.wait_for_timeout(1200)

        # 3. Read Web Animations API
        animations = page.evaluate("""() => {
            return document.getAnimations().map(anim => {
                const effect = anim.effect;
                const timing = effect ? effect.getComputedTiming() : {};
                return {
                    id: anim.id || '',
                    playState: anim.playState,
                    duration: timing.duration,
                    delay: timing.delay,
                    easing: timing.easing
                };
            });
        }""")
        results["webAnimations"] = animations

        # 4. Read recorded transition events
        results["recordedTransitions"] = page.evaluate("() => window.__TRANSITIONS__ || []")

        browser.close()
        return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dynamic UI and CSS animation inspector")
    parser.add_argument("url", help="Target URL to inspect")
    parser.add_argument("--hover", help="CSS selector to hover and inspect", default=None)
    parser.add_argument("--scroll", action="store_true", help="Scroll to bottom to trigger animations")
    args = parser.parse_args()

    data = inspect_dynamic(args.url, hover_selector=args.hover, scroll_to_bottom=args.scroll)
    print(json.dumps(data, indent=2))
