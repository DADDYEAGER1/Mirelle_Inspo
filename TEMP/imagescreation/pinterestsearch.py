import json
import webbrowser
import time
import urllib.parse
import os
from pathlib import Path
from PIL import Image
import threading
from queue import Queue

# Paths
JSON_INPUT_FOLDER = r"C:\Users\gaurav verma\Downloads\imagestocreate"
DOWNLOAD_FOLDER = r"C:\Users\gaurav verma\Downloads\download"
OUTPUT_BASE = r"C:\Users\gaurav verma\mirelle baby\mirelle-site\public\images\blog"

# Settings
WAIT_TIME_BETWEEN_SEARCHES = 5  # seconds between searches
MAX_FILE_SIZE_KB = 100  # Maximum file size in KB
WEBP_QUALITY_START = 85  # Starting quality for WebP

# Global variables
filename_queue = Queue()
processing_active = True
current_slug = ""

def get_available_jsons():
    """Get all JSON files from input folder"""
    json_files = {}
    json_folder = Path(JSON_INPUT_FOLDER)
    
    if not json_folder.exists():
        print(f"❌ JSON folder not found: {JSON_INPUT_FOLDER}")
        return {}
    
    idx = 1
    for json_file in json_folder.glob("*.json"):
        # Skip hero-images.json
        if json_file.name == "hero-images.json":
            continue
        
        slug = json_file.stem  # filename without extension
        json_files[str(idx)] = {
            "name": slug.replace("-", " ").title(),
            "file": json_file.name,
            "slug": slug
        }
        idx += 1
    
    return json_files

def select_json_file():
    """Let user select which JSON file to process"""
    json_files = get_available_jsons()
    
    if not json_files:
        print("❌ No JSON files found!")
        return None
    
    print(f"\n{'='*70}")
    print("📁 SELECT BLOG CATEGORY TO PROCESS")
    print(f"{'='*70}")
    print("\nAvailable categories:")
    for key, value in json_files.items():
        print(f"  {key}. {value['name']}")
    print(f"{'='*70}\n")
    
    while True:
        choice = input(f"Enter your choice (1-{len(json_files)}): ").strip()
        
        if choice in json_files:
            return json_files[choice]
        else:
            print(f"❌ Invalid choice! Please enter a number between 1 and {len(json_files)}")

def smart_crop(img, target_width, target_height):
    """Smart crop to exact dimensions from center"""
    original_width, original_height = img.size
    target_aspect = target_width / target_height
    original_aspect = original_width / original_height
    
    if original_aspect > target_aspect:
        # Image is wider - fit height and crop width
        new_height = original_height
        new_width = int(original_height * target_aspect)
    else:
        # Image is taller - fit width and crop height
        new_width = original_width
        new_height = int(original_width / target_aspect)
    
    # Center crop
    left = (original_width - new_width) // 2
    top = (original_height - new_height) // 2
    right = left + new_width
    bottom = top + new_height
    
    cropped_img = img.crop((left, top, right, bottom))
    final_img = cropped_img.resize((target_width, target_height), Image.LANCZOS)
    
    return final_img

def resize_and_convert_to_webp(input_path, output_path, target_dimensions):
    """Resize image to fit dimensions (smart crop if needed) and convert to WebP under 100KB"""
    try:
        with Image.open(input_path) as img:
            original_width, original_height = img.size
            print(f"      Original size: {original_width}x{original_height}px")
            
            # Convert to RGB if needed
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Smart crop to target dimensions
            target_width, target_height = target_dimensions
            print(f"      Target dimensions: {target_width}x{target_height}px")
            print(f"      Smart cropping to fit...")
            
            final_img = smart_crop(img, target_width, target_height)
            
            final_width, final_height = final_img.size
            print(f"      Final size: {final_width}x{final_height}px ✓")
            
            # Optimize to under 100KB as WebP
            print(f"      Optimizing to under {MAX_FILE_SIZE_KB}KB as WebP...")
            
            for quality in range(WEBP_QUALITY_START, 20, -5):
                final_img.save(output_path, 'WEBP', quality=quality, method=6)
                file_size_kb = os.path.getsize(output_path) / 1024
                
                if file_size_kb <= MAX_FILE_SIZE_KB:
                    print(f"      ✓ Saved at quality {quality}, size: {file_size_kb:.1f}KB")
                    return True
            
            # Last resort: very low quality
            final_img.save(output_path, 'WEBP', quality=10, method=6)
            file_size_kb = os.path.getsize(output_path) / 1024
            print(f"      ⚠ Saved at quality 10, size: {file_size_kb:.1f}KB")
            return True
            
    except Exception as e:
        print(f"      ✗ Error processing image: {e}")
        return False

def get_oldest_image(folder):
    """Get the oldest unprocessed image from folder"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}
    
    files = []
    for f in Path(folder).iterdir():
        if f.is_file() and f.suffix.lower() in image_extensions:
            files.append(f)
    
    if not files:
        return None
    
    # Sort by creation time (oldest first)
    files.sort(key=lambda x: x.stat().st_ctime)
    return files[0]

def search_amazon(query):
    """Open Amazon search in browser"""
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.amazon.com/s?k={encoded_query}"
    webbrowser.open(url)
    print(f"  → Searching Amazon: {query}")

def extract_search_query(filename):
    """Extract search query from filename (remove extension, keep hyphens as spaces)"""
    # Remove extension
    query = filename.replace('.webp', '').replace('.jpg', '').replace('.png', '').replace('.jpeg', '')
    # Replace hyphens with spaces
    query = query.replace('-', ' ')
    return query

def file_watcher_thread():
    """Background thread that watches for new files and processes them"""
    global processing_active, current_slug
    processed_count = 0
    
    output_folder = Path(OUTPUT_BASE) / current_slug
    output_folder.mkdir(parents=True, exist_ok=True)
    
    while processing_active or not filename_queue.empty():
        if filename_queue.empty():
            time.sleep(1)
            continue
        
        # Get next expected filename and dimensions
        expected_filename, dimensions = filename_queue.get()
        
        print(f"\n   [FILE WATCHER] Waiting for download #{processed_count + 1}: {expected_filename}")
        
        # Wait for a file to appear in download folder
        while processing_active:
            oldest_img = get_oldest_image(DOWNLOAD_FOLDER)
            if oldest_img:
                break
            time.sleep(2)
        
        if not processing_active and not oldest_img:
            break
        
        print(f"   [FILE WATCHER] Found: {oldest_img.name}")
        
        # Change extension to .webp
        base_name = expected_filename.rsplit('.', 1)[0]
        new_filename = f"{base_name}.webp"
        
        output_path = output_folder / new_filename
        
        # Delete existing file if exists
        if output_path.exists():
            print(f"   [FILE WATCHER] Deleting existing: {new_filename}")
            output_path.unlink()
        
        print(f"   [FILE WATCHER] Processing → {new_filename}")
        
        if resize_and_convert_to_webp(oldest_img, output_path, dimensions):
            # Delete original after successful processing
            oldest_img.unlink()
            processed_count += 1
            print(f"   [FILE WATCHER] ✓ Completed! ({processed_count} files processed)")
        else:
            print(f"   [FILE WATCHER] ✗ Failed to process!")
        
        filename_queue.task_done()

def process_json_category(selected_json):
    """Process selected JSON category"""
    global current_slug
    
    json_file_path = Path(JSON_INPUT_FOLDER) / selected_json['file']
    current_slug = selected_json['slug']
    
    print(f"\n✓ Selected: {selected_json['name']}")
    print(f"✓ JSON file: {json_file_path}")
    print(f"✓ Output folder: {OUTPUT_BASE}\\{current_slug}")
    
    # Load JSON file
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            images = json.load(f)
    except Exception as e:
        print(f"❌ Error reading JSON file: {e}")
        return False
    
    if not isinstance(images, list):
        print(f"❌ JSON should contain an array of image objects")
        return False
    
    total_images = len(images)
    print(f"\nTotal images to process: {total_images}\n")
    
    try:
        search_count = 0
        for i, img_data in enumerate(images, 1):
            filename = img_data.get('filename')
            width = img_data.get('width')
            height = img_data.get('height')
            
            if not filename:
                print(f"⚠ Skipping image #{i}: No filename")
                continue
            
            # Skip hero images
            if 'hero' in filename.lower():
                print(f"⚠ Skipping hero image: {filename}")
                continue
            
            search_count += 1
            
            # Use dimensions from JSON or default
            if width and height:
                dimensions = (int(width), int(height))
            else:
                dimensions = (800, 800)
                print(f"⚠ No dimensions for {filename}, using default 800x800")
            
            # Add to queue for file watcher
            filename_queue.put((filename, dimensions))
            
            # Extract search query
            search_query = extract_search_query(filename)
            
            print(f"\n[SEARCH {search_count}/{total_images}]")
            print(f"   Filename: {filename}")
            print(f"   Dimensions: {dimensions[0]}x{dimensions[1]}px")
            search_amazon(search_query)
            
            # Wait before next search (except last one)
            if search_count < total_images:
                print(f"   Waiting {WAIT_TIME_BETWEEN_SEARCHES} seconds before next search...")
                time.sleep(WAIT_TIME_BETWEEN_SEARCHES)
        
        print(f"\n✓ All searches completed!")
        print(f"⏳ Waiting for all downloads to complete...")
        
        # Wait for all files to be processed
        filename_queue.join()
        
        print(f"\n{'='*70}")
        print(f"🎉 CATEGORY '{selected_json['name'].upper()}' COMPLETED!")
        print(f"{'='*70}\n")
        return True
        
    except KeyboardInterrupt:
        print("\n\n⚠ Script interrupted by user!")
        return False

def main():
    global processing_active
    
    print(f"\n{'='*70}")
    print(f"🔍 BLOG IMAGE AMAZON SEARCH & PROCESSOR")
    print(f"{'='*70}")
    
    # Select JSON file
    selected_json = select_json_file()
    
    if not selected_json:
        return
    
    # Start file watcher thread
    print(f"\n{'='*70}")
    print("👀 Starting file watcher thread...")
    print(f"{'='*70}")
    watcher = threading.Thread(target=file_watcher_thread, daemon=True)
    watcher.start()
    
    try:
        # Process the category
        category_completed = process_json_category(selected_json)
        
        # Loop to allow processing multiple categories
        while category_completed:
            print(f"\n{'='*70}")
            response = input("Process another category? (yes/no): ").strip().lower()
            
            if response not in ['yes', 'y']:
                print("\n✓ Exiting. Thank you!")
                break
            
            # Select next JSON file
            selected_json = select_json_file()
            if not selected_json:
                break
            
            # Process next category
            category_completed = process_json_category(selected_json)
        
        # Signal done
        processing_active = False
        watcher.join(timeout=5)
        
    except KeyboardInterrupt:
        print("\n\n⚠ Script interrupted by user!")
        processing_active = False
        watcher.join(timeout=5)

if __name__ == "__main__":
    main()