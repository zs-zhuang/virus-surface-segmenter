#! /usr/bin/python3

import os, sys, math, string

import numpy as np,  scipy.ndimage

from scipy.misc import imshow
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image

from PIL import Image, ImageOps
import cv2
###from skimage.feature import corner_harris, corner_subpix, corner_peaks


#########################################################################################

in_arg = sys.argv[1]
name = in_arg+'.jpeg'
img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)

r = 16
r2 = 2*r +1

b = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, r2, r)

#ret,th1 = cv2.threshold(img,20,80,cv2.THRESH_BINARY)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,29,14)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,29,14)



b2 = scipy.misc.toimage(b)
b2.save('AdaptiveThreshold'+str(r)+'_virus_image.jpeg')
