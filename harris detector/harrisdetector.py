# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:16:22 2018

@author: Mansi Agarwal
"""

import cv2
import numpy as np

#preprocess image to greyscale and float32 type
img = cv2.imread('download.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#apply harris corner detector parameters- (image,windowsize,aperture parameter of sobel derivative, k=parameter reqd to compute R )
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()