"""Print resume/resume.html to assets/Pedro-H-Pinto-Resume.pdf.

Run from the repo root:  python3 resume/build_pdf.py
Needs: pip install playwright && playwright install chromium
"""
import pathlib
from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).resolve().parent.parent
src = root / "resume" / "resume.html"
out = root / "assets" / "Pedro-H-Pinto-Resume.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(src.as_uri(), wait_until="networkidle")
    page.evaluate("document.fonts.ready")
    page.pdf(path=str(out), format="Letter", print_background=True, prefer_css_page_size=True)
    browser.close()

print(f"wrote {out}")
