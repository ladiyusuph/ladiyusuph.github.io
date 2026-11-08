#!/usr/bin/env python3
"""Builds the standalone site in site/ from index.html, ready for static hosting.

index.html is the source for the page. Edit that file, then run: python3 build.py
"""
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SITE = ROOT / "site"
URL = "https://ladiyusuph.github.io/"
TITLE = "Ladi Yusuph, React Native developer and mobile team lead"
DESCRIPTION = "React Native developer and mobile team lead, building since 2022: offline-first apps, on-device AI, and responsive-rn, an open source library on npm."

source = (ROOT / "index.html").read_text()
# Everything up to the end of the page's <style> goes in <head>; the rest is the body.
head, body = source.split("</style>", 1)
head += "</style>"
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
head = head.replace("<title>Ladi Yusuph</title>", f"<title>{TITLE}</title>")

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{DESCRIPTION}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:image" content="{URL}assets/share.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<style>body {{ margin: 0; }} img {{ max-width: 100%; }}</style>
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""

if SITE.exists():
    shutil.rmtree(SITE)
shutil.copytree(ROOT / "assets", SITE / "assets")
(SITE / "index.html").write_text(page)
print(f"Built {SITE}")

missing = page.count("[add:")
if missing:
    print(f"Not ready to publish: {missing} [add: ...] placeholders still in the page.")
    sys.exit(1)
