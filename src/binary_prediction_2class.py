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
in_position = 'position_'+in_arg
in_prediction = 'prediction_'+in_arg

i = cv2.imread(in_image) #force read all image as color image, including gray scale
#i = io.imread(name)
#i = Image.open(in_image).convert('L')
new_i = np.copy(i)
#print(i.shape)

position_array = np.loadtxt(in_position)
prediction_array = np.loadtxt(in_prediction)

length = position_array.shape[0]
print(length)

#########################################################################################
# loop over positions, check the corresponding prediction, if prediction = 1, color the pixel

#for i in range (0, 100000):
for i in range (0,length):
    x = int(position_array[i][0])
    y = int(position_array[i][1])
    tag = int(prediction_array[i])
    if tag == -1:
        r = 0
        g = 0
        b = 0
        new_i[x,y] = [r, g, b]
        new_color = new_i[x,y]
    if tag == 1:
        r = 255
        g = 255
        b = 255
        new_i[x,y] = [r, g, b]
        new_color = new_i[x,y]

scipy.misc.toimage(new_i, cmin=0.0, cmax=...).save('binary.jpeg')
