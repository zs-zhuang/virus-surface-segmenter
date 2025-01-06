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
crop = 0

in_image = in_arg+'.jpeg'
in_position = 'ring_position_train_bad'

i = cv2.imread(in_image) #force read all image as color image, including gray scale
new_i = np.copy(i)

position_array = np.loadtxt(in_position)


length = position_array.shape[0]
print(length)

#########################################################################################
# loop over positions, check the corresponding prediction, if prediction = 1, color the pixel

#for i in range (0, 100000):
for i in range (0,length):
	#location = position_array[i]
	#print(location)
	x = int(position_array[i][0])			
	y = int(position_array[i][1])
	r = 0
	g = 255
	b = 255
	new_i[x,y] = [r, g, b] # set color value of pixel at position xy to r,g,b
	new_color = new_i[x,y]
	#print(new_color)

	
c1 = scipy.misc.toimage(new_i)
c1.save('check.jpeg')


