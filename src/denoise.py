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


#permform mean filter (blur image, reduce resolution which could mean reduce noise)
#initialize mean filter size 2 by 2 (higher filter size causes more blur image)
k = np.ones((2,2))/1

# perform convolution
b = scipy.ndimage.filters.convolve(img,k)

#perform median filter (get rid of specks or salt pepper noise)
c = scipy.ndimage.filters.median_filter(b,size=5,footprint=None,output=None,mode='reflect',cval=0.0,origin=0)



c2 = scipy.misc.toimage(c)
c2.save('denoise_'+str(in_arg)+'.jpeg')
