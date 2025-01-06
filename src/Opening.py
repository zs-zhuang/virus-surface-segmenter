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

#img2 = cv2.threshold(img, 50, 200, cv2.THRESH_BINARY)

kernel = np.ones((3,3),np.uint8)
b = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

b2 = scipy.misc.toimage(b)
b2.save('Opening_'+str(in_arg)+'.jpeg')
