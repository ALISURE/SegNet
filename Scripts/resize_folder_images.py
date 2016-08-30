#!/usr/bin/python
from PIL import Image
import os, sys

path= "/home/ubuntu/SegNet/CamVid/trainannot/"
path_other="/home/ubuntu/SegNet/CamVid/train_resizedannot/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            #f, e = os.path.splitext(path+item)
            imResize = im.resize((120,90), Image.ANTIALIAS)
            imResize.save("/home/ubuntu/SegNet/CamVid/train_resizedannot/"+item , 'JPEG', quality=90)

resize()
