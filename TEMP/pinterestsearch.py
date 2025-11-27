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
JSON_FILE = r"C:\Users\gaurav verma\Downloads\filenames.json"
DOWNLOAD_FOLDER = r"C:\Users\gaurav verma\Downloads\download"
OUTPUT_FOLDER = r"C:\Users\gaurav verma\Downloads\new files"

# Settings
WAIT_TIME_BETWEEN_SEARCHES = 5  # seconds between Pinterest searches
MAX_FILE_SIZE_KB = 100  # Maximum file size in KB
WEBP_QUALITY_START = 85  # Starting quality for WebP

# Global queue for file processing
filename_queue = Queue()
processing_active = True

def extract_search_query(filename):
    """Remove .webp and convert to search query"""
    query = filename.replace('.webp', '')
    query = query.replace('-', ' ')
    return query

def search_pinterest(query):
    """Open Pinterest search in browser"""
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.pinterest.com/search/pins/?q={encoded_query}"
    webbrowser.open(url)
    print(f"  → Searching: {query}")

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

def upscale_and_optimize(input_path, output_path, target_filename):
    """Upscale image and optimize to under 100KB as WebP"""
    try:
        with Image.open(input_path) as img:
            # Get original dimensions
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
            
            # Try different upscale factors and qualities to stay under 100KB
            best_img = None
            best_quality = WEBP_QUALITY_START
            
            # Start with 2x upscale
            scale_factor = 2
            new_width = original_width * scale_factor
            new_height = original_height * scale_factor
            
            print(f"      Upscaling to: {new_width}x{new_height}px")
            upscaled_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Try to save with decreasing quality until under 100KB
            for quality in range(WEBP_QUALITY_START, 20, -5):
                upscaled_img.save(output_path, 'WEBP', quality=quality)
                file_size_kb = os.path.getsize(output_path) / 1024
                
                if file_size_kb <= MAX_FILE_SIZE_KB:
                    print(f"      ✓ Saved at quality {quality}, size: {file_size_kb:.1f}KB")
                    return True
            
            # If still too large, try with original size
            print(f"      Trying original size to meet 100KB limit...")
            for quality in range(WEBP_QUALITY_START, 20, -5):
                img.save(output_path, 'WEBP', quality=quality)
                file_size_kb = os.path.getsize(output_path) / 1024
                
                if file_size_kb <= MAX_FILE_SIZE_KB:
                    print(f"      ✓ Saved at quality {quality}, size: {file_size_kb:.1f}KB (original size)")
                    return True
            
            # Last resort: very low quality
            img.save(output_path, 'WEBP', quality=10)
            file_size_kb = os.path.getsize(output_path) / 1024
            print(f"      ⚠ Saved at quality 10, size: {file_size_kb:.1f}KB")
            return True
            
    except Exception as e:
        print(f"      ✗ Error processing image: {e}")
        return False

def file_watcher_thread():
    """Background thread that watches for new files and processes them"""
    global processing_active
    processed_count = 0
    
    while processing_active or not filename_queue.empty():
        if filename_queue.empty():
            time.sleep(1)
            continue
        
        # Get next expected filename
        expected_filename = filename_queue.get()
        
        print(f"\n   [FILE WATCHER] Waiting for download #{processed_count + 1}...")
        
        # Wait for a file to appear in download folder
        while processing_active:
            oldest_img = get_oldest_image(DOWNLOAD_FOLDER)
            if oldest_img:
                break
            time.sleep(2)
        
        if not processing_active and not oldest_img:
            break
        
        print(f"   [FILE WATCHER] Found: {oldest_img.name}")
        
        # Process and rename the image
        output_path = Path(OUTPUT_FOLDER) / expected_filename
        print(f"   [FILE WATCHER] Processing → {expected_filename}")
        
        if upscale_and_optimize(oldest_img, output_path, expected_filename):
            # Delete original after successful processing
            oldest_img.unlink()
            processed_count += 1
            print(f"   [FILE WATCHER] ✓ Completed! ({processed_count} files processed)")
        else:
            print(f"   [FILE WATCHER] ✗ Failed to process!")
        
        filename_queue.task_done()

def process_category(category_name, items):
    """Process all items in a category"""
    total = len(items)
    print(f"\n{'='*70}")
    print(f"📂 CATEGORY: {category_name.upper()}")
    print(f"{'='*70}")
    print(f"Total images: {total}")
    print(f"Processing order: First to Last (ID order)\n")
    
    # Sort by id (first to last)
    items_sorted = sorted(items, key=lambda x: x.get('id', 0))
    
    for i, item in enumerate(items_sorted, 1):
        img_id = item.get('id')
        filename = item.get('filename')
        
        # Add filename to queue for file watcher
        filename_queue.put(filename)
        
        # Extract search query and search Pinterest
        search_query = extract_search_query(filename)
        
        print(f"\n[SEARCH {i}/{total}] ID: {img_id}")
        search_pinterest(search_query)
        
        # Wait before next search (except for last one)
        if i < total:
            print(f"   Waiting {WAIT_TIME_BETWEEN_SEARCHES} seconds before next search...")
            time.sleep(WAIT_TIME_BETWEEN_SEARCHES)
    
    print(f"\n✓ Search completed for category: {category_name}")

def main():
    global processing_active
    
    # Create output folder if doesn't exist
    Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)
    
    # Load JSON file
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return
    
    # Get all categories
    categories = list(data.keys())
    total_categories = len(categories)
    
    print(f"\n{'='*70}")
    print(f"🎯 SUPER PINTEREST AUTOMATION SCRIPT")
    print(f"{'='*70}")
    print(f"Download folder: {DOWNLOAD_FOLDER}")
    print(f"Output folder: {OUTPUT_FOLDER}")
    print(f"Max file size: {MAX_FILE_SIZE_KB}KB")
    print(f"\nFound {total_categories} categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat} ({len(data[cat])} images)")
    
    # Start file watcher thread
    print(f"\n{'='*70}")
    print("🔍 Starting file watcher thread...")
    print(f"{'='*70}")
    watcher = threading.Thread(target=file_watcher_thread, daemon=True)
    watcher.start()
    
    try:
        # Process each category
        for i, category_name in enumerate(categories, 1):
            items = data[category_name]
            
            # Process the category (searches Pinterest and queues filenames)
            process_category(category_name, items)
            
            # Wait for all files in this category to be processed
            print(f"\n⏳ Waiting for all downloads in this category to complete...")
            filename_queue.join()
            
            # Wait for confirmation before next category (except for last one)
            if i < total_categories:
                print(f"\n{'='*70}")
                input(f"✓ Category complete! Press ENTER to start next category ({i+1}/{total_categories})... ")
            else:
                print(f"\n{'='*70}")
                print("🎉 ALL CATEGORIES COMPLETED!")
                print(f"{'='*70}\n")
        
        # Signal that we're done
        processing_active = False
        watcher.join(timeout=5)
        
    except KeyboardInterrupt:
        print("\n\n⚠ Script interrupted by user!")
        processing_active = False
        watcher.join(timeout=5)

if __name__ == "__main__":
    main()