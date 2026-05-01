"""
Watch & Organize — Hero + Body Images
--------------------------------------
1. Choose: Hero or Body images
2. Pick a slug from the list
3. Drop images one by one into the watch folder
4. Each image is center-cropped → 800x800 → converted to WebP (<100KB)
5. Saved to: OUTPUT_BASE / slug / filename.webp
6. After slug is done, asks which slug to do next

Requirements:
    pip install Pillow

Usage:
    python watch_and_organize.py
"""

import json
import time
import threading
from pathlib import Path
from PIL import Image

# ── CONFIG ────────────────────────────────────────────────────────────────────
WATCH_FOLDER  = Path(r"C:\Users\Ryzen\Downloads\drop_here")
HERO_JSON     = Path(r"D:\portfolio\hero_images_summer.json")
BODY_JSON     = Path(r"D:\portfolio\body_images_summer.json")
OUTPUT_BASE   = Path(r"D:\portfolio\mirelle-site\public\images\blog")
POLL_INTERVAL = 1
MAX_KB        = 100
TARGET_SIZE   = (800, 800)
# ─────────────────────────────────────────────────────────────────────────────

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tiff"}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_new_images(folder: Path) -> list:
    files = [
        f for f in folder.iterdir()
        if f.is_file()
        and f.suffix.lower() in IMAGE_EXTENSIONS
        and not f.name.startswith("_converting_")
    ]
    files.sort(key=lambda f: f.stat().st_mtime)
    return files


def center_crop_and_resize(img: Image.Image, size=(800, 800)) -> Image.Image:
    """Center-crop to 1:1 then resize to target size."""
    w, h = img.size
    min_dim = min(w, h)
    left   = (w - min_dim) // 2
    top    = (h - min_dim) // 2
    right  = left + min_dim
    bottom = top  + min_dim
    img = img.crop((left, top, right, bottom))
    img = img.resize(size, Image.LANCZOS)
    return img


def convert_to_webp(src: Path, dest: Path, max_kb: int = 100, crop: bool = True) -> bool:
    max_bytes = max_kb * 1024
    try:
        img = Image.open(src).convert("RGB")
        if crop:
            img = center_crop_and_resize(img, TARGET_SIZE)
        elif img.size != TARGET_SIZE:
            img = center_crop_and_resize(img, TARGET_SIZE)
        # else: hero image already 800x800, leave as-is
        for quality in range(85, 9, -5):
            img.save(dest, "WEBP", quality=quality, method=6)
            if dest.stat().st_size <= max_bytes:
                print(f"    🔄 WebP @ quality={quality} → {dest.stat().st_size // 1024}KB")
                return True
        # Fallback: scale down further
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


def process_image(image_path: Path, dest_folder: Path, target_name: str, crop: bool = True) -> threading.Thread:
    def _run():
        final_name = target_name + ".webp"
        final_path = dest_folder / final_name
        temp_path  = image_path.parent / ("_converting_" + image_path.name)
        try:
            image_path.rename(temp_path)
        except Exception as e:
            print(f"  ❌ Could not lock {image_path.name}: {e}")
            return
        convert_to_webp(temp_path, final_path, MAX_KB, crop=crop)
        try:
            temp_path.unlink()
        except Exception:
            pass
        print(f"  ✓  Saved: {dest_folder.name}/{final_name}\n")

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return t


def pick_mode() -> str:
    print("\n" + "═" * 60)
    print("  What do you want to process?")
    print("  1. Hero images")
    print("  2. Body images")
    print("═" * 60)
    while True:
        choice = input("  Enter 1 or 2: ").strip()
        if choice == "1":
            return "hero"
        elif choice == "2":
            return "body"
        print("  ❌ Invalid. Enter 1 or 2.")


def pick_slug(data: dict, done: set) -> str | None:
    slugs = list(data.keys())
    remaining = [s for s in slugs if s not in done]
    if not remaining:
        return None

    print("\n" + "─" * 60)
    print("  Available slugs:")
    for i, slug in enumerate(remaining, 1):
        count = len(data[slug]) if isinstance(data[slug], list) else 1
        print(f"  {i}. {slug}  ({count} image{'s' if count != 1 else ''})")
    print("─" * 60)

    while True:
        choice = input("  Pick a slug number (or 'q' to quit): ").strip()
        if choice.lower() == "q":
            return "quit"
        if choice.isdigit() and 1 <= int(choice) <= len(remaining):
            return remaining[int(choice) - 1]
        print("  ❌ Invalid choice.")


def get_image_list(data: dict, slug: str, mode: str) -> list:
    """Return ordered list of target filenames (no extension) for the slug."""
    entry = data.get(slug, {})
    if mode == "hero":
        name = entry.get("hero_image", "")
        return [name] if name else []
    else:
        return entry if isinstance(entry, list) else []


def watch_slug(slug: str, image_list: list, crop: bool = True):
    dest_folder = OUTPUT_BASE / slug
    dest_folder.mkdir(parents=True, exist_ok=True)
    print(f"\n  📁 Created/confirmed folder: {dest_folder}")

    total          = len(image_list)
    index          = 0
    active_threads = []

    print(f"\n  📋 {total} image(s) to process for [{slug}]")
    print(f"  ⏳ Waiting for image 1/{total}: {image_list[0]}\n")

    while index < total:
        active_threads = [t for t in active_threads if t.is_alive()]
        new_images = get_new_images(WATCH_FOLDER)

        if new_images:
            img         = new_images[0]
            target_name = image_list[index]

            print(f"  📥 Received : {img.name}")
            print(f"     → Rename : {target_name}.webp")

            t = process_image(img, dest_folder, target_name, crop=crop)
            active_threads.append(t)
            index += 1

            if index < total:
                print(f"  ⏳ Waiting for image {index+1}/{total}: {image_list[index]}\n")
        else:
            print(f"\r  ⏳ Drop image {index+1}/{total}: {image_list[index]}", end="", flush=True)

        time.sleep(POLL_INTERVAL)

    for t in active_threads:
        t.join()

    print(f"\n\n  ✅ All {total} image(s) done for [{slug}]")


def main():
    WATCH_FOLDER.mkdir(parents=True, exist_ok=True)

    print(f"\n  📂 Watch folder : {WATCH_FOLDER}")
    print(f"  💾 Output base  : {OUTPUT_BASE}")

    mode = pick_mode()
    data = load_json(HERO_JSON if mode == "hero" else BODY_JSON)

    print(f"\n  ✅ Loaded {'hero' if mode == 'hero' else 'body'} JSON — {len(data)} slug(s) found")

    done = set()

    while True:
        slug = pick_slug(data, done)
        if slug is None:
            print("\n  🎉 All slugs processed!")
            break
        if slug == "quit":
            print("\n  👋 Exiting.")
            break

        image_list = get_image_list(data, slug, mode)
        if not image_list:
            print(f"  ⚠️  No images found for [{slug}], skipping.")
            done.add(slug)
            continue

        watch_slug(slug, image_list, crop=(mode == "body"))
        done.add(slug)

        remaining = len(data) - len(done)
        if remaining == 0:
            print("\n  🎉 All slugs done!")
            break

        print(f"\n  {remaining} slug(s) remaining.")


if __name__ == "__main__":
    main()
