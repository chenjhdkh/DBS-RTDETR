import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('/mnt/workspace/RTDETR-main/ultralytics/cfg/models/rt-detr/DBS-RTDETR.yaml')
    # model.load('') # loading pretrain weights
    model.train(data='/mnt/workspace/RTDETR-main/dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=150,
                batch=4,
                workers=4,
                device='0',
                # resume='', # last.pt path
                project='runs/train',
                name='exp',
                )