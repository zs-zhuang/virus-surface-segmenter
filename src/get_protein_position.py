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
r = 3

in_image = in_arg+'.jpeg'

out_position = "protein_position_"+in_arg
out_file = open (out_position, 'w')

i = cv2.imread(in_image, cv2.IMREAD_GRAYSCALE)

row, col = i.shape
print(row, col)

#########################################################################################

for m in range (r, row-r):
    for n in range (r, col-r):
        I = i[m, n]
        if I > 150:
            out_file.write(str(m)+' '+str(n)+'\n')

