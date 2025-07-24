# Military Object Detection & Augmentation Project

## Overview
This project focuses on building an **AI-model for accurately detecting military assets such as vehicles, soldiers and helicopters**. Our project consists of 3 primary components:

1. **Autoencoder** – For feature extraction, anomaly detection, and file size reduction.
2. **Markdown Documentation Tool** – For a streamlined annotation process of dataset assets.
3. **Image Augmentation Tool** – To convert dataset assets into PNG, and provide augmentation via Pillow
---

## Objectives
- data compression, image denoising, anomaly detection and facial recognition
- Improve model robustness through advanced data augmentation.
- Streamline data annotation to aid in neural network training.

---

## Components

### Autoencoder Tool
- Compresses image data to lower dimensions for efficient storage and training.
- Detects anomalies by comparing reconstruction error.
- Implemented in **TensorFlow** for efficient and easy modification.

### Markdown Tool
- Generates **Manually annotated images** aiding in the model-training process


### Image Augmentation Tool
- Creates **additional training data** for the AI model through subtle augmentations to existing data. 



##  Augmentation Tool
The produced script augments an image dataset by applying a series of random transformations to each image in the input folders (`train`, `test`, `valid`). For every image, it performs operations such as horizontal and vertical flips, 90° rotations, brightness and contrast adjustments, and adds Gaussian noise. Each original image is augmented 5 to increase dataset diversity. The script preserves the original dataset structure by saving augmented images in a separate output folder (`dataset/augment`), ensuring that each augmented image has a unique name. 


##  Autoencoder Tool
The script cleans an image dataset with  a  series  of preprocessing steps to offer high-quality, normalized data. It begins by deleting  unreadable or damaged images by double-verifying them using PIL. It continues  to detect and exclude  out-of-focus images based on sharpness indicator. It then deletes duplicate files using a process called MD5 hashing. For the rest of the correct images, the script resizes them to a standard resolution (512×512), convert them to RGB, and save them as PNG files in a separate processed folder with an  appropriate naming scheme. 

##  Annotation Tool

This python program  performs a GUI image annotation tool to  generate  "COCO-style" datasets. Images  are loaded, which can then be labeled  with bounding boxes or polygons. Each annotation is stored in the COCO JSON format. It  includes  image navigation support, autosave  of annotations, and exporting  the entire dataset into one  file called: "coco_annotations.json". It also provides the functionality to label each bounding box with a series of pre-set labels such as "Military Vehicle" or "Military Helicopter".
