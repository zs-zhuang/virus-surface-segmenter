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

######################################################################################

#perform median filter (get rid of specks or salt pepper noise)
#m = scipy.ndimage.filters.median_filter(b,size=2,footprint=None,output=None,mode='reflect',cval=0.0,origin=0)

#perform log transformation to enhance contrast (only use this if contrast is so low that naked eyes basically cannot see anything)
l = a2
l_max = np.max(l) #get max value of l
l2 = (255.0*np.log(1+l))/np.log(1+l_max) #perform log transofrmation
l3 = l2.astype(int) # converted to type int

#perform contrast stretching to enhace contrast (replaces log transformation)
c = a2
c_max = c.max() #find max pixel value
c_min = c.min() #find min pixel value
#c2 = d.astype(float32)
c2 = 255*(c-c_min)/(c_max-c_min) #contrast stretching transformation

#########################################################################################
#convert from an ndarray to an image

I_l3 = scipy.misc.toimage(l3)
I_c2 = scipy.misc.toimage(c2)

I_l3.save('log_'+str(in_arg)+'.jpeg')
I_c2.save('stretch_'+str(in_arg)+'.jpeg')
