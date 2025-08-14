import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

if __name__ == '__main__':
    model = RTDETR('') # select your model.pt path
    model.predict(source='/mnt/workspace/VisDrone2019/data/images/test',
                  conf=0.25,
                  project='runs/detect',
                  name='exp',
                  save=True,
                #   visualize=True # visualize model features maps
                  )