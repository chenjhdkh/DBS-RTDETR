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
Pre-trained Weights: The primary model weights (best.pt) required to reproduce the key findings of this study can be downloaded from the Releases page of this repository.
```

## Dataset& Preprocessing

```
/dataset/
├── datasetsar/       # Experimental dataset
├── data.yaml         # Dataset configuration file
├── split_data.py     # Script to split training/validation/test sets
├── xml2txt.py        # Convert XML annotations to TXT format
└── yolo2coco.py      # Convert YOLO format to COCO format
```

Prepare the dataset & Preprocessing:
1. The SAR-AIRcraft-1.0 dataset used in this research is open-access. Please refer to the original publication for download details.
2. Edit `data.yaml` to specify image paths and class information.
3. Run `split_data.py` to standardize the training, validation, and test set splits.
4. Use `xml2txt.py` or `yolo2coco.py` to convert annotations into the required format.

## Usage

### step1. Setup Environment

Install dependencies: 

`pip install -r requirements.txt `

### step2. Configure Training
<img width="1582" height="634" alt="b3e676139e18c2614d65bccc87bd1dce" src="https://github.com/user-attachments/assets/1c0d66e8-78b6-4dbe-84ac-34a203ba2471" />
Configuration Files:
Model configuration file:

`DBS-RTDETR\RTDETR-main\ultralytics\cfg\models\rt-detr\DBS-RTDETR.yaml`

Dataset configuration file:

`DBS-RTDETR\RTDETR-main\dataset\data.yaml`

### step3. Train DBS-RTDETR

`python train.py`

###  step4. Evaluate DBS-RTDETR

`python val.py `

## Rusults

Below are some sample detection results using the trained DBS-RTDETR model on SAR aircraft images:

<img width="1230" height="390" alt="result" src="https://github.com/user-attachments/assets/a4339dd4-fc35-41dd-b03e-9fab1c3e564d" />
