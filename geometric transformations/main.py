#geometric transformations

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#SCALING
img = cv.imread('messi5.jpg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("rescaled", res)
cv.waitKey(0)
cv.destroyAllWindows()

#inter_cubic is  for zooming
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

#TRANSLATIOM
img = cv.imread('messi5.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])  #HERE 100 is transation in x, and 50 is translation in y
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#ROTATION
img = cv.imread('messi5.jpg',0)
rows,cols = img.shape
M = cv.getRotationMatrix2D((cols/2,rows/2),90,1)  #getRotationMatrix2D(center, angle, scale)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

#AFFINE TRANSFORMATION
img = cv.imread('messi5.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])  #pts1 holds the pixel locations of i/p image
pts2 = np.float32([[10,100],[200,50],[100,250]]) #pts2 holds the posns where pts1 should be affined to
M = cv.getAffineTransform(pts1,pts2) #3 relations bw (x,y) and (x',y') gives 6 eqns which gives the 6 parameters
dst = cv.warpAffine(img,M,(cols,rows))
plt.imshow(img),plt.title('Input')
plt.imshow(dst),plt.title('Output')
plt.show()

#HOMOGRAPHY
img = cv.imread('messi5.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()