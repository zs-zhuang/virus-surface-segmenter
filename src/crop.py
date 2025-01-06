#! /usr/bin/python3

import os, sys, math, string

import numpy as np,  scipy.ndimage

from scipy.misc.pilutil import Image
from skimage import io

from PIL import Image, ImageOps

import scipy.misc
import cv2

###from skimage.feature import corner_harris, corner_subpix, corner_peaks


#########################################################################################

in_arg = sys.argv[1]

crop = 3

in_image = in_arg+'.jpeg'

img = cv2.imread(in_image) #force read all image as color image, including gray scale
cols, rows, _ = img.shape
#########################################################################################

# crop out the outer frame due to r
crop = img[crop:cols-crop, crop:rows-crop]

#Save positive images
c1 = scipy.misc.toimage(crop)
c1.save('crop_'+in_image)
