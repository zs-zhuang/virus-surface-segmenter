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


#in_arg = sys.argv[1]
#name = 'colorLabel_BW2_fix_virus_image.jpeg' 
name = 'colorLabel_ring_virus_image.jpeg'
a1 = cv2.imread(name)
#a2 = a1.astype(float)
print(a1.shape)



######################################################################################

out_position1 = "position_train_good"
out_position2 = "position_train_bad"
out_file1 = open (out_position1, 'w')
out_file2 = open(out_position2, 'w')


row, col, _ = a1.shape


for m in range (0, row):
    for n in range (0, col):
            Ixy = a1[m, n]
            #print(Ixy)
            if Ixy[0] == 0 and Ixy[1] == 0 and Ixy[2] == 254:
                out_file1.write(str(m)+' '+str(n)+'\n')
            #if Ixy[0] == 0 and Ixy[1] == 255 and Ixy[2] == 0 :
            if Ixy[0] == 0 and Ixy[1] == 255 and Ixy[2] == 0 or Ixy[0] == 1 and Ixy[1] == 255 and Ixy[2] == 0 or Ixy[0] == 0 and Ixy[1] == 254 and Ixy[2] == 0 or Ixy[0] == 2 and Ixy[1] == 255 and Ixy[2] == 1 or Ixy[0] == 1 and Ixy[1] == 255 and Ixy[2] == 1 :
                out_file2.write(str(m)+' '+str(n)+'\n')



