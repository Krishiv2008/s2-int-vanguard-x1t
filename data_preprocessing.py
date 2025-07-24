import os
import shutil
import hashlib
import cv2
from PIL import Image, UnidentifiedImageError

# Mapping input to output folders
FOLDER_MAP = {
    "dataset/train": "dataset/processed/train",
    "dataset/test": "dataset/processed/test",
    "dataset/valid": "dataset/processed/valid"
}

IMG_EXTS = {'.jpg', '.jpeg', '.png'}
STANDARD_SIZE = (512, 512)
VARIANCE_THRESHOLD = 100  # Lower = blurrier

# --- 1. Remove Corrupt ---
def is_valid_image(filepath):
    try:
        with Image.open(filepath) as img:
            img.verify()
        return True
    except (UnidentifiedImageError, IOError, OSError):
        return False

# --- 2. Remove Blurry ---
def is_blurry(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return True
    variance = cv2.Laplacian(img, cv2.CV_64F).var()
    return variance < VARIANCE_THRESHOLD

# --- 3. Remove Duplicates ---
def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

# --- 4. Resize & Convert ---
def process_image(src_path, dst_path):
    with Image.open(src_path) as img:
        img = img.convert("RGB")
        img = img.resize(STANDARD_SIZE)
        dst_path = os.path.splitext(dst_path)[0] + ".png"
        img.save(dst_path, "PNG")

# --- 5. Main Cleaning ---
def clean_dataset():
    all_images = []
    hashes_seen = set()

    for raw_dir, out_dir in FOLDER_MAP.items():
        os.makedirs(out_dir, exist_ok=True)
        img_counter = 0

        for root, _, files in os.walk(raw_dir):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext not in IMG_EXTS:
                    continue
                src = os.path.join(root, file)
                if not is_valid_image(src) or is_blurry(src):
                    continue
                h = file_hash(src)
                if h in hashes_seen:
                    continue
                hashes_seen.add(h)
                clean_name = f"img_{img_counter:06}.png"
                dst = os.path.join(out_dir, clean_name)
                process_image(src, dst)
                all_images.append(dst)
                img_counter += 1

    return all_images

# --- Run all ---
if __name__ == "__main__":
    print("Cleaning dataset into separate folders...")
    clean_imgs = clean_dataset()
    print(f"Total cleaned: {len(clean_imgs)}")
