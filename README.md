Enhanced Aircraft Target Detection in SAR Images via Deep Butterfly Convolution and Edge Information Fusion
This repository contains the implementation of the algorithm proposed in our paper:

Enhanced Aircraft Target Detection in SAR Images via Deep Butterfly Convolution and Edge Information Fusion Authors: Baobao Liu, Mengxin Chen, Fengping Wang, Chenchao Chang, Xinqing Li.

Overview
This code implements our proposed approach for robust and accurate aircraft target detection in Synthetic Aperture Radar (SAR) images.

Requirements
python >= 3.8
torch >= 1.10
torchvision
numpy
opencv-python
tqdm
Install dependencies: pip install -r requirements.txt
Files
├── train.py          # Train the model
├── detect.py      # Run detection on images
├── models/           # Model definition files
├── utils/            # Helper functions
└── README.md
Dataset
/dataset/
├── data.yaml         # Dataset configuration file
├── split_data.py     # Script to split training/validation/test sets
├── xml2txt.py        # Convert XML annotations to TXT format
└── yolo2coco.py      # Convert YOLO format to COCO format
Prepare the dataset:

Edit data.yaml to specify image paths and class information.
Run split_data.py to split the dataset.
Use xml2txt.py or yolo2coco.py to convert annotations into the required format.
Usage
Run the training script:

python train.py
The script will automatically load the dataset from dataset/data.yaml and use the DBS-RTDETR.yaml configuration file. Trained weights and logs will be saved under runs/train/exp.
