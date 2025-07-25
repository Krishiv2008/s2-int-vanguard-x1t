# Vanguard Defense Internship 
## s2-int-vanguard-x1t
Welcome to the repository for the Vanguard Defense Internship under the Harvard Undergraduate Ventures TECH Summer Program (HUVTSP). This file documents the entire workflow, datasets, and code.

## 1. Datasets
Our datasets span four critical areas of modern sensing and defense technology. Drone/ISR imagery involves collecting real-time visuals from unmanned aerial systems for surveillance and reconnaissance operations. Aerial/SAR imagery focuses on synthetic aperture radar, which captures high-resolution ground images regardless of weather or lighting conditions. Automotive radar explores how radar systems in vehicles detect and track objects in their surroundings to support autonomous navigation and collision avoidance. Lastly, RF signal/waveform analysis examines raw radio-frequency signals to identify, classify, or decode transmissions—vital for communications, electronic warfare, and spectrum intelligence.
<br>
<br>
<br>
<br>

### Drone/ISR Imagery

### 1. VisDrone2019 Dataset

The VisDrone2019 dataset is a large-scale benchmark for drone-based computer vision, created by the AISKYEYE team at Tianjin University. It is designed for civilian applications like aerial surveillance, agriculture, and photography.

#### Key Features:
The dataset includes 288 video clips (261,908 frames) and 10,209 static images.

#### Diversity: 
Data was captured by various drone models across 14 different cities in China, covering diverse urban and rural environments under different weather and lighting conditions.

#### Annotations: Contains over 2.6 million manually annotated bounding boxes for 10 object categories, including pedestrians, cars, bicycles, and buses.

#### Tasks: The dataset is structured to support several computer vision tasks such as object detection, object tracking, and crowd counting.

#### Download Instructions

The dataset is available from multiple sources. The easiest way to get started is via Kaggle. For official development kits and alternative download mirrors, use the GitHub repository.

#### Kaggle Download:

You can download the dataset directly from Kaggle at the following link:
https://www.kaggle.com/datasets/kushagrapandya/visdrone-dataset

#### Official GitHub Repository:

For evaluation tools, detailed information, and official download links (via Google Drive and BaiduYun), visit the main project repository:

https://github.com/VisDrone/VisDrone-Dataset
<br>
<br>


### 2. Military Vehicle Recognition Dataset
The Military Vehicle Recognition dataset is a collection of labeled aerial images for computer vision tasks, created by the MilitaryVehicleRecognition team on Roboflow. It is designed for defense and security applications like automated surveillance and reconnaissance.

#### Key Features:

The dataset includes labeled aerial images of military objects such as air fighters, bombers, armored personnel carriers, tanks, and soldiers.

#### Diversity:

Data was captured by reconnaissance drones during the Russo-Ukrainian War, simulating real-world conditions with diverse altitudes, angles, and lighting across various scenarios.

#### Annotations: 

Contains manually annotated bounding boxes for object categories including air fighters, bombers, armored personnel carriers, tanks, and soldiers.

#### Tasks: 

The dataset is structured to support computer vision tasks such as object detection and classification, aiding in real-time decision-making for surveillance and situational awareness.

#### Download Instructions

The dataset is available directly from Roboflow Universe. For access to the images, trained models, and deployment options, use the project page.

Roboflow Download:

You can access and download the dataset from Roboflow at the following link: 

https://universe.roboflow.com/militaryvehiclerecognition/military-vehicle-recognition

Official Project Page:

For detailed information, metrics, and browse options (including the specific query parameters), visit the main project page:

https://universe.roboflow.com/militaryvehiclerecognition/military-vehicle-recognition
<br>
<br>

### 3. Drone Object Detection (YOLO)
This dataset was created for the "Amateur Drone Detection and Tracking" project in 2019. It is specifically designed for training object detection models based on the YOLO (You Only Look Once) architecture.


#### Key Features: 
The dataset includes over 4,000 images of amateur drones, such as those from the DJI Phantom series.

#### Negative Samples:
It also contains images of non-drone, "negative" objects that may resemble drones, which helps to reduce false positives during detection.

#### Compatibility: 
The dataset was tested with YOLOv2-tiny and YOLOv3-voc and is well-suited for use with the Darknet framework.

#### Purpose: 
Primarily used for building and training models to detect and track amateur unmanned aerial vehicles (UAVs).

#### Download & License

#### Kaggle Download:

You can download the dataset directly from Kaggle at the following link:
https://www.kaggle.com/datasets/sshikamaru/drone-yolo-detection

#### License:

This dataset is available under the Creative Commons Attribution 4.0 International license. You can view the full license details here:
https://creativecommons.org/licenses/by/4.0/legalcode.en
<br>
<br>
<br>
<br>

###  Aerial/SAR imagery

### 4. OpenEarthMap-SAR / IEEE GRSS 2025 Track 1
This large-scale dataset is designed for land cover classification using both synthetic aperture radar (SAR) and aerial imagery. It was developed for Track 1 of the IEEE GRSS Data Fusion Contest 2025 and supports high-resolution segmentation tasks. The dataset's goal is to advance all-weather land cover mapping by leveraging the unique capabilities of SAR to penetrate clouds and operate in any lighting conditions.

#### Key Features:

The dataset contains over 4,000 paired images, including 8-bit grayscale SAR images (1024x1024px) and 8-bit color RGB aerial images. Umbra Lab, Inc. provides the SAR imagery, while the RGB images come from NAIP (USA), IGN (France), and GSI (Japan). The data covers 35 regions with a ground sampling distance of 0.15 to 0.5 meters.
Annotations: It includes pseudo-labels for 8 distinct land cover classes, which were generated using OpenEarthMap models. Manually labeled regions are also available for validation.

#### Land Cover Classes: 
The 8 classes are Bareland, Rangeland, Developed Space, Road, Tree, Water, Agricultural Land, and Building.
#### Tasks: 
The primary focus is on developing robust methods for all-weather land cover mapping, with a special emphasis on using SAR data for segmentation and classification.


#### Download & License
The dataset is available for download from Kaggle. For official contest information and alternative downloads, refer to the Zenodo repository.

#### Kaggle Download:
You can download the dataset directly from Kaggle at the following link:

https://www.kaggle.com/datasets/forekid/dfc25-track1-trainval

#### Official Repository:

The official dataset for the IEEE GRSS DFC 2025 Track 1 is hosted on Zenodo:

https://zenodo.org/records/14622048

#### Licensing:

The SAR imagery is licensed under CC BY 4.0 (© 2024 Umbra Lab, Inc.), while the RGB imagery from various national sources is under CC BY 2.0

<br>
<br>
<br>
<br>

###  Automotive Radar

### 5. Oxford Radar RobotCar Dataset

The Oxford Radar RobotCar dataset is a radar-focused extension of the original Oxford RobotCar Dataset. It contains real-world driving data collected from a vehicle traversing a 280 km route through Oxford, UK, and is designed to accelerate research into autonomous vehicle technology.

#### Key Features:

Why it's useful: This dataset is ideal for developing AI for autonomous vehicles and ground robots. It focuses on radar, a sensor that is robust in adverse weather conditions like fog, rain, or snow that can challenge vision and lidar systems.

#### Data Type:
It includes a comprehensive sensor suite with data from a Navtech Millimetre-Wave FMCW scanning radar, two Velodyne lidar sensors, six cameras, and a GPS/INS system.
#### Size: 
The complete dataset is 4.7 TB, though smaller sample datasets are also available for download.

#### Download & License

#### Download Link:

You can access the dataset, documentation, and development tools from the official project website:
https://oxford-robotics-institute.github.io/radar-robotcar-dataset/

#### License:
The dataset is released under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License and is intended for non-commercial academic use only.
<br>
<br>

### 6. The RadarScenes Dataset

The RadarScenes dataset contains recordings from four automotive radar sensors and a single front-facing camera, captured from a measurement vehicle. The data was recorded between 2016 and 2018 in Ulm, Germany, and is designed to support research in autonomous driving, particularly for object detection and scene understanding using raw radar data.

#### Key Features:

The dataset provides synchronized data from four automotive radar sensors, odometry sensors, and one front-facing documentary camera. It provides point-wise annotations for moving road users.

#### Size: 
This is a large-scale dataset containing over 4 hours of driving data. It covers 100 km across 158 different scenarios, and its overall size is comparable to other major driving datasets like nuScenes.

#### Data Structure: 
Recordings are organized into sequences. Radar and odometry data are stored in HDF5 files, with metadata available in scenes.json, sensor.json, and sequences.json files. Camera images are located in a separate subfolder, with filenames corresponding to their timestamps.

#### Tasks: 
It is particularly useful for developing and testing algorithms for object detection, sensor fusion, and environmental perception directly from radar sensor outputs.


#### Download & License

#### Kaggle Download:

You can download the dataset directly from Kaggle at the following link:
https://www.kaggle.com/datasets/aleksandrdubrovin/the-radarscenes-data-set

#### License:
This dataset is available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0).
<br>
<br>

### 7. UDayton24Automotive Dataset

The UDayton24Automotive dataset provides raw and demosaicked image pairs from automotive-grade cameras for object detection research. It was created to facilitate the development of algorithms that can work directly with raw sensor data and to study cross-camera performance between different color filter arrays (RGGB and RCCB).

#### Key Features:
The dataset is composed of three main parts:
RGGB Camera Data (Baseline Training Set): 438 training and 88 testing images from a SONY IMX390 camera with an RGGB filter and a 174-degree fisheye lens.
RCCB Camera Data (Test Set): 474 images from a camera with an RCCB filter and a 169-degree fisheye lens, used for evaluation.
Joint RGGB-RCCB Camera Data: 90 paired images from a dual-camera setup for cross-camera training tasks.

#### Size: 
The dataset contains a total of 1,090 images across the different subsets.

#### Annotations:
The images are manually annotated with bounding boxes for four object classes: cars, pedestrians, stop signs, and traffic lights.

#### Tasks:
It is primarily designed for training and evaluating object detection algorithms on raw sensor data, especially for tasks involving knowledge distillation and domain adaptation between different camera sensor technologies.

#### Download & License

#### Kaggle Download:
You can download the dataset directly from Kaggle at the following link:
https://www.kaggle.com/datasets/setarehkian/udayton24automotive-datasets/data

#### License:
The dataset is available under an open license: Database: Open Database, Contents: © Original Authors.

<br>
<br>
<br>
<br>

###  RF Signal/ Waveform

### 8. RF Signal Data

This dataset contains radio frequency (RF) signal data collected over approximately one month. The data was acquired using Software Defined Radio (SDR) hardware connected to DragonOS Focal, a Linux distribution for SDR enthusiasts.

#### Key Features:
The dataset features a collection of radio frequency signal data captured between May 5, 2023, and June 11, 2023.

#### Data Source:
All signals were recorded using SDR hardware, making it representative of real-world captures.

#### Tasks:
This type of data is valuable for training machine learning models for tasks in signal intelligence (SIGINT), spectrum monitoring, and interference detection. It can be used to develop algorithms that classify different types of wireless signals.

#### Download & License

#### Kaggle Download:

You can download the dataset directly from Kaggle at the following link:
https://www.kaggle.com/datasets/suraj520/rf-signal-data

#### License:
The license for this dataset is not explicitly specified on the download page.

<br>
<br>

### 9. RadioML 2016.10A Dataset
The RadioML 2016.10A dataset is a collection of simulated radio signals. It includes a variety of common communication modulations, such as AM and FM, making it a foundational resource for machine learning in radio communications.

#### Key Features:
This dataset is ideal for training AI models to identify and classify signals, which is a core task in electronic warfare (EW) and signal intelligence (SIGINT). It helps develop systems capable of automatically recognizing different types of transmissions.

#### Data Type: 
It consists of raw In-phase and Quadrature (I/Q) signal data. Each sample is labeled with its specific modulation type and the signal-to-noise ratio (SNR) at which it was generated.

#### Size: 
The dataset is approximately 600 MB.

#### Download & License

#### Download Link:
You can download the dataset and access related resources from the official DeepSig website:
https://www.deepsig.ai/datasets

#### License:
The dataset is available for research purposes under a permissive, MIT-like license.





