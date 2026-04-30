"""
Extract hero image info from mothers-day blog posts.
Reads frontmatter from .md files, saves to hero_images_md_nails.json

Usage:
    python extract_hero_images.py
"""

import json
import re
from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────
BLOGS_FOLDER = Path(r"D:\portfolio\mirelle-site\src\content\blogs")
OUTPUT_FILE  = Path(r"D:\portfolio\hero_images_md_nails.json")
SEARCH_TERM  = "mothers-day"
# ─────────────────────────────────────────────────────────────────────────────


def parse_frontmatter(text: str) -> dict:
    """Extract key: value pairs from YAML frontmatter block."""
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
    """Return simplified ratio string like 16:9, 4:3, 1:1 etc."""
    try:
        w, h = int(width), int(height)
        from math import gcd
        g = gcd(w, h)
        return f"{w // g}:{h // g}"
    except Exception:
        return "unknown"


def main():
    results = {}

    md_files = sorted(BLOGS_FOLDER.glob("*.md"))
    matched  = [f for f in md_files if SEARCH_TERM in f.stem]

    if not matched:
        print(f"❌ No files found matching '{SEARCH_TERM}' in {BLOGS_FOLDER}")
        return

    print(f"✅ Found {len(matched)} matching files:\n")

    for md_file in matched:
        text = md_file.read_text(encoding="utf-8")
        fm   = parse_frontmatter(text)

        image     = fm.get("image", "")
        image_alt = fm.get("imageAlt", "")
        width     = fm.get("imageWidth", "")
        height    = fm.get("imageHeight", "")
        ratio     = get_ratio(width, height)
        filename  = image.split("/")[-1] if image else ""

        results[md_file.stem] = {
            "hero_image"  : filename,
            "url"         : image,
            "imageAlt"    : image_alt,
            "imageWidth"  : int(width)  if width.isdigit()  else width,
            "imageHeight" : int(height) if height.isdigit() else height,
            "ratio"       : ratio,
        }

        print(f"  📄 {md_file.stem}")
        print(f"     🖼️  {filename}")
        print(f"     📐 {width} x {height}  ({ratio})\n")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"💾 Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
