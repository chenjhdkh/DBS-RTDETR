# Enhanced Aircraft Target Detection in SAR Images via Deep Butterfly Convolution and Edge Information Fusion

This repository contains the implementation of the algorithm proposed in our paper:

**Enhanced Aircraft Target Detection in SAR Images via Deep Butterfly Convolution and Edge Information Fusion**
Authors: Baobao Liu, Mengxin Chen, Fengping Wang, Chenchao Chang, Xinqing Li.

## Overview

This code implements our proposed approach for robust and accurate aircraft target detection in Synthetic Aperture Radar (SAR) images.

## Requirements

```
python >= 3.8
torch >= 1.10
torchvision
numpy
opencv-python
tqdm
Install dependencies: pip install -r requirements.txt
```

## Files

```
├── train.py          # Train the model
├── detect.py      # Run detection on images
├── models/           # Model definition files
├── utils/            # Helper functions
└── README.md
```

## Dataset

```
/dataset/
├── datasetsar/       # Experimental dataset
├── data.yaml         # Dataset configuration file
├── split_data.py     # Script to split training/validation/test sets
├── xml2txt.py        # Convert XML annotations to TXT format
└── yolo2coco.py      # Convert YOLO format to COCO format
```

Prepare the dataset:

1. Edit `data.yaml` to specify image paths and class information.
2. Run `split_data.py` to split the dataset.
3. Use `xml2txt.py` or `yolo2coco.py` to convert annotations into the required format.

## Usage

### step1. Setup Environment

Install dependencies: 

`pip install -r requirements.txt `

### step2. Configure Training

Configuration Files:
<img width="920" height="482" alt="image-20250828202817478" src="https://github.com/user-attachments/assets/0552a780-e3db-4300-b13c-7100e0c5c251" />
Model configuration file:

`DBS-RTDETR\RTDETR-main\ultralytics\cfg\models\rt-detr\DBS-RTDETR.yaml`

Dataset configuration file:

`DBS-RTDETR\RTDETR-main\dataset\data.yaml`

### step3. Train DBS-RTDETR

`python train.py`

###  step4. Evaluate DBS-RTDETR

`python val.py `

