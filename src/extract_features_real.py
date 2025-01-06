#! /usr/bin/python3

import os, sys, math, string

import numpy as np,  scipy.ndimage

from scipy.misc.pilutil import Image
from skimage import io

from PIL import Image, ImageOps
import cv2
###from skimage.feature import corner_harris, corner_subpix, corner_peaks


#########################################################################################
#Open image and get basic info

in_arg = sys.argv[1] #example bad1, bad2, bad3, good1, good2
r = int(sys.argv[2]) #neighborhood size is (2r+1)^2
#t = sys.argv[3] #target value 1 for good colony pixel, -1 for bad colony pixel

print(r)

name1 = ""+in_arg+".jpeg"
name2 = "clahe_MorphClose4_lowpass30_"+in_arg+".jpeg"
name3 = "highpass1_clahe20_MorphClose4_lowpass30_"+in_arg+".jpeg"
#print(in_arg, r)


out_feature = "feature_"+in_arg
#out_target = "target_"+in_arg
out_position = "position_"+in_arg
out_file1 = open (out_feature, 'w')
#out_file2 = open(out_target, 'w')
out_file3 = open(out_position, 'w')

#filename1 = str(in_arg)
#print(filename)


a1 = cv2.imread(name1, cv2.IMREAD_GRAYSCALE)
a2 = cv2.imread(name2, cv2.IMREAD_GRAYSCALE)
a3 = cv2.imread(name3, cv2.IMREAD_GRAYSCALE)
#print(a1.shape, a2.shape, a3.shape)
#print(a1.dtype, a2.dtype, a3.dtype)
#print(a.mean())
#print(a.max())
#print(a.min())

#a_mean = a.mean()
print(a1.shape)
nrows, ncols = a1.shape
#print(nrows)
#print(ncols)

"""
if nrows <= ncols:
        r = int(nrows/200)
else:
        r = int(ncols/200)
"""
area = (2*r+1)**2

#print (a[0:3,0:2])


for x in range (r, nrows+1-r):
    for y in range(r, ncols+1-r):
        Ixy1 = a1[x, y]
        lowy = int(y-r)
        highy = int(y+r+1)
        lowx = int(x-r)
        highx = int(x+r+1)
        b1 = a1[lowx:highx,lowy:highy].copy()
        Imean1 = np.mean(b1)
        Istd1 = np.std(b1)
        nblack1 = (b1 < 70).sum()
        nwhite1 = (b1 > 90).sum()
        frac_black1 = nblack1/area
        frac_white1 = nwhite1/area
        #max_1 = np.amax(b1)
        #min_1 = np.amin(b1)
        #diff_1 = max_1 = min_1

        Ixy2 = a2[x, y]
        lowy = int(y-r)
        highy = int(y+r+1)
        lowx = int(x-r)
        highx = int(x+r+1)
        b2 = a2[lowx:highx,lowy:highy].copy()
        Imean2 = np.mean(b2)
        Istd2 = np.std(b2)
        nblack2 = (b2 < 90).sum()
        nwhite2 = (b2 > 170).sum()
        frac_black2 = nblack2/area
        frac_white2 = nwhite2/area

        Ixy3 = a3[x, y]
        lowy = int(y-r)
        highy = int(y+r+1)
        lowx = int(x-r)
        highx = int(x+r+1)
        b3 = a3[lowx:highx,lowy:highy].copy()
        Imean3 = np.mean(b3)
        Istd3 = np.std(b3)
        nblack3 = (b3 < 120).sum()
        nwhite3 = (b3 > 150).sum()
        frac_black3 = nblack3/area
        frac_white3 = nwhite3/area





        #out_file1.write(str(Ixy1)+' '+str(Imean1)+' '+str(Istd1)+' '+str(frac_black1)+' '+str(frac_white1)+' '+str(max_1)+' '+str(min_1)+' '+str(diff_1)+'\n')
        out_file1.write(str(Ixy1)+' '+str(Imean1)+' '+str(Istd1)+' '+str(frac_black1)+' '+str(frac_white1)+' '+str(Ixy2)+' '+str(Imean2)+' '+str(Istd2)+' '+str(frac_black2)+' '+str(frac_white2)+' '+str(Ixy3)+' '+str(Imean3)+' '+str(Istd3)+' '+str(frac_black3)+' '+str(frac_white3)+'\n')
        out_file3.write(str(x)+' '+str(y)+'\n')
