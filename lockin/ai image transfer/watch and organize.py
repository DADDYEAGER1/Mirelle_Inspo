"""
Hero Image Watcher
Shows the ordered list of hero images needed, then watches the folder.
Drop images one by one in the listed order — each gets renamed and moved to its slug folder.

Requirements:
    pip install Pillow

Usage:
    python watch_hero_images.py
"""

import json
import time
import threading
from pathlib import Path
from PIL import Image

# ── CONFIG ────────────────────────────────────────────────────────────────────
WATCH_FOLDER  = Path(r"C:\Users\Ryzen\Downloads\floral md nails]")
HERO_JSON     = Path(r"D:\portfolio\hero_images_md_nails.json")
POLL_INTERVAL = 1
MAX_KB        = 100
# ─────────────────────────────────────────────────────────────────────────────

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff"}


def load_hero_order(json_path: Path) -> list:
    """Returns ordered list of (slug, filename, ratio)."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    result = []
    for slug, info in data.items():
        result.append((slug, info["hero_image"], info.get("ratio", "?")))
    return result


def get_new_images(folder: Path) -> list:
    files = [
        f for f in folder.iterdir()
        if f.is_file()
        and f.suffix.lower() in IMAGE_EXTENSIONS
        and not f.name.startswith("_converting_")
    ]
    files.sort(key=lambda f: f.stat().st_mtime)
    return files


def convert_to_webp(src: Path, dest: Path, max_kb: int = 100) -> bool:
    max_bytes = max_kb * 1024
    try:
        img = Image.open(src).convert("RGB")
        for quality in range(85, 9, -5):
            img.save(dest, "WEBP", quality=quality, method=6)
            if dest.stat().st_size <= max_bytes:
                print(f"    🔄 WebP @ quality={quality} → {dest.stat().st_size // 1024}KB")
                return True
        scale = 0.9
        while scale > 0.2:
            w, h = img.size
            resized = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
            resized.save(dest, "WEBP", quality=10, method=6)
            if dest.stat().st_size <= max_bytes:
                print(f"    🔄 WebP @ scale={scale:.1f} → {dest.stat().st_size // 1024}KB")
                return True
            scale -= 0.1
        print(f"    ⚠️  Best effort, could not reach under {max_kb}KB")
        return True
    except Exception as e:
        print(f"    ❌ Conversion error: {e}")
        return False


def process_hero(image_path: Path, dest_folder: Path, target_name: str) -> threading.Thread:
    def _run():
        # Always save as webp
        final_name = Path(target_name).stem + ".webp"
        final_path = dest_folder / final_name
        temp_path  = image_path.parent / ("_converting_" + image_path.name)
        try:
            image_path.rename(temp_path)
        except Exception as e:
            print(f"  ❌ Could not lock {image_path.name}: {e}")
            return
        convert_to_webp(temp_path, final_path, MAX_KB)
        try:
            temp_path.unlink()
        except Exception:
            pass
        print(f"  ✓  Saved: {dest_folder.name}/{final_name}\n")

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return t


def print_order(heroes: list, current_index: int):
    """Print the full ordered list, marking done/current/pending."""
    print("\n" + "─" * 60)
    print("  #   Status     Slug")
    print("─" * 60)
    for i, (slug, filename, ratio) in enumerate(heroes):
        if i < current_index:
            status = "✅ done  "
        elif i == current_index:
            status = "👉 NEXT  "
        else:
            status = "   ...   "
        print(f"  {i+1:<3} {status}  {slug}  ({ratio})")
    print("─" * 60 + "\n")


def main():
    print(f"📂 Watch folder : {WATCH_FOLDER}")
    print(f"📋 Hero JSON    : {HERO_JSON}")
    print(f"{'─' * 60}")

    if not WATCH_FOLDER.exists():
        print(f"❌ Watch folder not found: {WATCH_FOLDER}")
        return

    heroes = load_hero_order(HERO_JSON)
    total  = len(heroes)
    print(f"✅ {total} hero images to process\n")

    # Show full list upfront
    print_order(heroes, 0)

    index          = 0
    active_threads = []

    while index < total:
        active_threads = [t for t in active_threads if t.is_alive()]

        slug, target_name, ratio = heroes[index]
        dest_folder = WATCH_FOLDER / slug

        new_images = get_new_images(WATCH_FOLDER)

        if new_images:
            img = new_images[0]  # take the first arrived image
            dest_folder.mkdir(exist_ok=True)

            print(f"📥 Image received: {img.name}")
            print(f"   → Slug   : {slug}")
            print(f"   → Rename : {Path(target_name).stem}.webp")
            print(f"   → Ratio  : {ratio}")

            t = process_hero(img, dest_folder, target_name)
            active_threads.append(t)
            index += 1

            if index < total:
                print_order(heroes, index)
                next_slug, next_file, next_ratio = heroes[index]
                print(f"⏳ Waiting for hero image #{index + 1}: [{next_slug}]  ({next_ratio})\n")
        else:
            slug_now, _, ratio_now = heroes[index]
            print(f"\r⏳ Waiting for image #{index + 1}: [{slug_now}]  ({ratio_now})", end="", flush=True)

        time.sleep(POLL_INTERVAL)

    for t in active_threads:
        t.join()

    print("\n\n✅ All hero images processed!")
    print_order(heroes, total)


if __name__ == "__main__":
    main()
