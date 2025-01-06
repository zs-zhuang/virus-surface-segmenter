#! /usr/bin/python3

import os, sys, math, string
from skimage.filters import threshold_otsu
import scipy.misc
from PIL import Image
import numpy as np
import cv2

in_arg = sys.argv[1]
name = ""+in_arg+".jpeg" 

img = cv2.imread(name, 0)

#blur = img
r = 5
blur = cv2.GaussianBlur(img,(r,r),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#th4 = cv2.erode(th3, None, iterations=1)


m = scipy.misc.toimage(th3)
m.save('otsu'+str(r)+'_'+in_arg+'.jpeg')
