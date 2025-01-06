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

in_arg = sys.argv[1] #example bad1, bad2, bad3, good1, good2
r = int(sys.argv[2]) #neighborhood size is (2r+1)^2
t = sys.argv[3] #target value 1 for good colony pixel, -1 for bad colony pixel
name = sys.argv[4] #good or bad

print(r)

in_image1 = ''+in_arg+'.jpeg'
in_image2 = 'clahe_MorphClose4_lowpass30_'+in_arg+'.jpeg'
in_image3 = 'highpass1_clahe20_MorphClose4_lowpass30_'+in_arg+'.jpeg'


in_position = 'ring_position_train_' + name

a1 = cv2.imread(in_image1, cv2.IMREAD_GRAYSCALE)
a2 = np.copy(a1)
b1 = cv2.imread(in_image2, cv2.IMREAD_GRAYSCALE) 
b2 = np.copy(b1)
c1 = cv2.imread(in_image3, cv2.IMREAD_GRAYSCALE)
c2 = np.copy(c1)



position_array = np.loadtxt(in_position)


length = position_array.shape[0]
print(length)


out_feature = "feature_train_"+name
out_file1 = open (out_feature, 'w')

out_target = "target_train_"+name
out_file2 = open (out_target, 'w')

nrows, ncols = a1.shape
area = (2*r+1)**2
#########################################################################################
# loop over positions, check the corresponding prediction, if prediction = 1, color the pixel

for i in range (0,length):
#for i in range (0,2):
    x = int(position_array[i][0])			
    y = int(position_array[i][1])
    Ixy_a = a2[x, y]
    Ixy_b = b2[x, y]
    Ixy_c = c2[x, y]
    if x > r and x < nrows+1-r and y > r and y < ncols+1-r:
        lowy = int(y-r)
        highy = int(y+r+1)
        lowx = int(x-r)
        highx = int(x+r+1)

        a3 = a2[lowx:highx,lowy:highy].copy()
        Imean_a = np.mean(a3)
        Istd_a = np.std(a3)
        nblack_a = (a3 < 70).sum()
        nwhite_a = (a3 > 90).sum()
        frac_black_a = nblack_a/area
        frac_white_a = nwhite_a/area
        #max_a = np.amax(a3)
        #min_a = np.amin(a3)
        #diff_a = max_a - min_a

        b3 = b2[lowx:highx,lowy:highy].copy()
        Imean_b = np.mean(b3)
        Istd_b = np.std(b3)
        nblack_b = (b3 < 90).sum()
        nwhite_b = (b3 > 170).sum()
        frac_black_b = nblack_b/area
        frac_white_b = nwhite_b/area


        c3 = c2[lowx:highx,lowy:highy].copy()
        Imean_c = np.mean(c3)
        Istd_c = np.std(c3)
        nblack_c = (c3 < 120).sum()
        nwhite_c = (c3 > 150).sum()
        frac_black_c = nblack_c/area
        frac_white_c = nwhite_c/area


        #out_file1.write(str(Ixy_a)+' '+str(Imean_a)+' '+str(Istd_a)+' '+str(frac_black_a)+' '+str(frac_white_a)+' '+str(max_a)+' '+str(min_a)+' '+str(diff_a)+'\n')
        out_file1.write(str(Ixy_a)+' '+str(Imean_a)+' '+str(Istd_a)+' '+str(frac_black_a)+' '+str(frac_white_a)+' '+str(Ixy_b)+' '+str(Imean_b)+' '+str(Istd_b)+' '+str(frac_black_b)+' '+str(frac_white_b)+' '+str(Ixy_c)+' '+str(Imean_c)+' '+str(Istd_c)+' '+str(frac_black_c)+' '+str(frac_white_c)+'\n')
        out_file2.write(str(t)+'\n')

