import os 
from PIL import Image, ImageEnhance 
import numpy as np
import random 


def random_horizontal_flip(image):
    if random.random() > 0.5:
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return image


def random_vertical_flip(image):
    if random.random() > 0.5:
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    return image


def random_rotate_90(image):
    angle = random.choice([0, 90, 180, 270])
    return image.rotate(angle, expand=True)


def random_brightness(image):
    enhancer = ImageEnhance.Brightness(image)
    factor = random.uniform(0.7, 1.3)
    return enhancer.enhance(factor)


def random_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    factor = random.uniform(0.7, 1.3)
    return enhancer.enhance(factor)


def add_gaussian_noise(image):
    np_image = np.array(image)
    mean = 0
    var = random.uniform(5, 20)
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, np_image.shape)
    noisy = np_image + gauss
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return Image.fromarray(noisy)


def augment_image_pil(image):
    image = random_horizontal_flip(image)
    image = random_vertical_flip(image)
    image = random_rotate_90(image)
    image = random_brightness(image)
    image = random_contrast(image)
    image = add_gaussian_noise(image)
    return image


def augment_dataset(input_folder, output_folder, augmentations_per_image=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]

    print(f"Found {len(image_files)} images in '{input_folder}'.")
    print(f"Generating {augmentations_per_image} augmented images per input image...")

    for img_name in image_files:
        try:
            img_path = os.path.join(input_folder, img_name)
            img = Image.open(img_path).convert('RGB')

            for i in range(augmentations_per_image):
                aug_img = augment_image_pil(img)
                base_name, ext = os.path.splitext(img_name)
                save_name = f"{base_name}_aug{i+1}{ext}"
                save_path = os.path.join(output_folder, save_name)
                aug_img.save(save_path)

        except Exception as e:
            print(f"Error processing '{img_name}': {e}")

    print(f"Augmentation completed. Augmented images saved to '{output_folder}'.")


if __name__ == "__main__":
    base_input_dir = "dataset"
    base_output_dir = "dataset/augment"
    subsets = ["train", "test", "valid"]
    augmentations_per_image = 5

    for subset in subsets:
        input_path = os.path.join(base_input_dir, subset)
        output_path = os.path.join(base_output_dir, subset)
        print(f"\n--- Augmenting {subset} set ---")
        augment_dataset(input_path, output_path, augmentations_per_image)