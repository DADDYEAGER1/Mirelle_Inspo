"""
Extract hero and body image info from summer blog posts.

Outputs:
  - hero_images_summer.json   (with dimensions)
  - body_images_summer.json   (filenames only, no extension)

Usage:
    python extract_images.py
"""

import json
import re
from math import gcd
from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────
BLOGS_FOLDER      = Path(r"D:\portfolio\mirelle-site\src\content\blogs")
HERO_OUTPUT_FILE  = Path(r"D:\portfolio\hero_images_summer.json")
BODY_OUTPUT_FILE  = Path(r"D:\portfolio\body_images_summer.json")
SEARCH_TERM       = "summer"

EXTRA_FILES = [
    Path(r"D:\portfolio\mirelle-site\src\content\blogs\beach-nails.md"),
    Path(r"D:\portfolio\mirelle-site\src\content\blogs\how-to-do-ombre-nails-at-home.md"),
]
# ─────────────────────────────────────────────────────────────────────────────


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def get_ratio(width: str, height: str) -> str:
    try:
        w, h = int(width), int(height)
        g = gcd(w, h)
        return f"{w // g}:{h // g}"
    except Exception:
        return "unknown"


def extract_body_images(text: str) -> list:
    body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.DOTALL)
    filenames = []
    for m in re.finditer(r"src=['\"]([^'\"]+)['\"]", body):
        src = m.group(1)
        raw = src.split("/")[-1]
        name = Path(raw).stem
        if name:
            filenames.append(name)
    return filenames


def main():
    hero_results = {}
    body_results = {}

    md_files = sorted(BLOGS_FOLDER.glob("*.md"))
    matched  = [f for f in md_files if SEARCH_TERM in f.stem]

    existing = {f.resolve() for f in matched}
    for extra in EXTRA_FILES:
        if extra.exists() and extra.resolve() not in existing:
            matched.append(extra)
        elif not extra.exists():
            print(f"  Warning: extra file not found: {extra}")

    if not matched:
        print(f"No files found matching '{SEARCH_TERM}' in {BLOGS_FOLDER}")
        return

    print(f"Found {len(matched)} file(s):\n")

    for md_file in matched:
        text = md_file.read_text(encoding="utf-8")
        fm   = parse_frontmatter(text)

        image     = fm.get("image", "")
        image_alt = fm.get("imageAlt", "")
        width     = fm.get("imageWidth", "")
        height    = fm.get("imageHeight", "")
        ratio     = get_ratio(width, height)
        filename  = Path(image.split("/")[-1]).stem if image else ""

        hero_results[md_file.stem] = {
            "hero_image" : filename,
            "url"        : image,
            "imageAlt"   : image_alt,
            "imageWidth" : int(width)  if width.isdigit()  else width,
            "imageHeight": int(height) if height.isdigit() else height,
            "ratio"      : ratio,
        }

        body_images = extract_body_images(text)
        body_results[md_file.stem] = body_images

        print(f"  {md_file.stem}")
        print(f"    Hero : {filename}  ({width}x{height}, {ratio})")
        print(f"    Body : {len(body_images)} image(s)\n")

    HERO_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    HERO_OUTPUT_FILE.write_text(json.dumps(hero_results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Hero saved to : {HERO_OUTPUT_FILE}")

    BODY_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    BODY_OUTPUT_FILE.write_text(json.dumps(body_results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Body saved to : {BODY_OUTPUT_FILE}")


if __name__ == "__main__":
    main()
