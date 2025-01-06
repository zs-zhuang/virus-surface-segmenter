#! /usr/bin/python3

import os, sys, math, string

import numpy as np,  scipy.ndimage

from scipy.misc.pilutil import Image
from skimage import io
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from PIL import Image, ImageOps

###from skimage.feature import corner_harris, corner_subpix, corner_peaks


#########################################################################################

# Import data 
featurefile = 'train_feature_data' #multi column file that contains feature values
targetfile = 'train_target_data' #single column file that specify whether a pixel is part of a good colony 1 or bad colony -1

X = np.loadtxt(featurefile)
Y = np.loadtxt(targetfile)

X = X.astype(np.float32)
Y = Y.astype(np.int32)


from sklearn import model_selection as ms
#X_train, X_test, Y_train, Y_test = ms.train_test_split(X, Y, test_size=0.2, random_state=55)
X_train, X_test, Y_train, Y_test = ms.train_test_split(X, Y, test_size=0.5)


part1_feature = ('part1_'+featurefile)
part1_target =('part1_'+targetfile)
np.savetxt(part1_feature, X_train)
np.savetxt(part1_target, Y_train)


part2_feature = ('part2_'+featurefile)
part2_target =('part2_'+targetfile)
np.savetxt(part2_feature, X_test)
np.savetxt(part2_target, Y_test)

