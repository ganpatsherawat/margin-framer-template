import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import json
from playwright.sync_api import sync_playwright

def inspect():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto("https://essential-time-088020.framer.app/", wait_until="networkidle")
        page.wait_for_timeout(2000)

        # Extract links
        links = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a')).map(a => ({
                text: a.innerText.trim(),
                href: a.href,
                className: a.className
            }));
        }""")

        # Extract all text blocks
        texts = page.evaluate("""() => {
            const elements = Array.from(document.querySelectorAll('h1, h2, h3, h4, p, span, blockquote, a, button'));
            return elements.map(el => ({
                tag: el.tagName,
                text: el.innerText.trim(),
                classes: el.className
            })).filter(x => x.text.length > 0 && x.text.length < 500);
        }""")

        # Extract all image sources
        images = page.evaluate("""() => {
            const imgs = Array.from(document.querySelectorAll('img')).map(img => ({
                src: img.src,
                srcset: img.srcset,
                alt: img.alt,
                naturalWidth: img.naturalWidth,
                naturalHeight: img.naturalHeight
            }));
            const bgImgs = Array.from(document.querySelectorAll('*')).map(el => {
                const bg = window.getComputedStyle(el).backgroundImage;
                return bg && bg !== 'none' ? bg : null;
            }).filter(Boolean);
            return { imgs, bgImgs };
        }""")

        # Extract computed fonts and tokens
        tokens = page.evaluate("""() => {
            const rootStyle = window.getComputedStyle(document.documentElement);
            const bodyStyle = window.getComputedStyle(document.body);
            return {
                bodyFont: bodyStyle.fontFamily,
                h1Font: document.querySelector('h1') ? window.getComputedStyle(document.querySelector('h1')).fontFamily : '',
                colors: {
                    bodyBg: bodyStyle.backgroundColor,
                    bodyColor: bodyStyle.color,
                }
            };
        }""")

        data = {
            "title": page.title(),
            "links": links,
            "images": images,
            "tokens": tokens,
            "texts_sample": texts[:60]
        }

        with open(r"d:\margin-framer-template\original-extract.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Extracted {len(links)} links, {len(images['imgs'])} images, {len(texts)} text elements.")
        print(f"Page title: {page.title()}")
        browser.close()

if __name__ == "__main__":
    inspect()
