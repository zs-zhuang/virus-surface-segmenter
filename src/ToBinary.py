#! /usr/bin/python3

import os, sys, math, string

import numpy as np,  scipy.ndimage

from scipy.misc import imshow
import scipy.fftpack as fftim
from scipy.misc.pilutil import Image
import cv2
from PIL import Image, ImageOps

###from skimage.feature import corner_harris, corner_subpix, corner_peaks


#########################################################################################

in_arg = sys.argv[1]
name = in_arg+'.jpeg'
a1 = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
a2 = a1.astype(float)
thresh = 100

######################################################################################

#perform median filter (get rid of specks or salt pepper noise)
#m = scipy.ndimage.filters.median_filter(b,size=2,footprint=None,output=None,mode='reflect',cval=0.0,origin=0)


row, col = a2.shape
print(a2.shape)

for m in range (0, row):
    for n in range (0, col):
            Ixy = a2[m, n]
            #I = int(Ixy)
            if Ixy <= thresh:
                a2[m, n] = 0
            if Ixy >thresh:
                a2[m, n] = 255



#########################################################################################
#convert from an ndarray to an image

a3 = scipy.misc.toimage(a2)
a3.save('BW_'+str(in_arg)+'.jpeg')

in_image = 'BW_'+str(in_arg)+'.jpeg'
a4 = cv2.imread(in_image)
a5 = scipy.misc.toimage(a4)
a5.save('BW2_'+str(in_arg)+'.jpeg')

