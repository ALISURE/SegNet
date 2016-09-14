#!/usr/bin/python
from PIL import Image
import os, sys

path= "/home/ubuntu/SegNet/CamVid/ADEChallengeData2016/annotations/training/"
path_other="/home/ubuntu/SegNet/CamVid/ADEChallengeData2016/annotations/training/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            #f, e = os.path.splitext(path+item)
            imResize = im.resize((672,512), Image.ANTIALIAS)
            imResize.save("/home/ubuntu/SegNet/CamVid/ADEChallengeData2016/annotations/training-back/"+item , 'PNG', quality=90)

resize()
