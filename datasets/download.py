import kagglehub

# List of Kaggle dataset slugs
datasets = {
    "Drone YOLO Detection": "sshikamaru/drone-yolo-detection",
    "DFC25 Track1": "forekid/dfc25-track1-trainval",
    "VisDrone": "kushagrapandya/visdrone-dataset",
    "RF Signal Data": "suraj520/rf-signal-data",
    "RadarScenes": "aleksandrdubrovin/the-radarscenes-data-set",
    "UDayton24 Automotive": "setarehkian/udayton24automotive-datasets"
}

# Download each dataset
for name, slug in datasets.items():
    print(f"Downloading: {name} ({slug})")
    path = kagglehub.dataset_download(slug)
    print(f"{name} saved at: {path}\n")