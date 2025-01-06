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
in_position = 'protein_position_denoise_binary'

i = cv2.imread(in_image) #force read all image as color image, including gray scale
new_i = np.copy(i)
print(i.shape)

position_array = np.loadtxt(in_position)

length = position_array.shape[0]
print(length)

#########################################################################################
# loop over positions, check the corresponding prediction, if prediction = 1, color the pixel

for i in range (0,length):
    x = int(position_array[i][0])
    y = int(position_array[i][1])
    r = 0
    g = 255
    b = 255
    new_i[x,y] = [r, g, b]
    #print(new_i[x,y])
    new_color = new_i[x,y]

#save new highlight image with predicted colonies colored in red
scipy.misc.toimage(new_i, cmin=0.0, cmax=...).save('color.jpeg')

#Now I want to make the blue color transparent so that I can still see the original colony under the blue color
background = cv2.imread(in_image)
overlay = cv2.imread('color.jpeg')

added_image = cv2.addWeighted(background,0.0,overlay,1.0,0)

cv2.imwrite('transparent_prediction.jpeg', added_image)

#Lastly, crop away the outer frame with width r
img1 = cv2.imread('transparent_prediction.jpeg')
img2 = cv2.imread(in_image)
cols, rows, _ = img1.shape
print(cols, rows)

# crop out the outer frame due to r
crop_highlight = img1[crop:cols-crop, crop:rows-crop]
crop_original = img2[crop:cols-crop, crop:rows-crop]

#Save positive images
c1 = scipy.misc.toimage(crop_highlight)
c1.save('denoise_final_prediction.jpeg')
c2 = scipy.misc.toimage(crop_original)
c2.save('denoise_final_original.jpeg')
