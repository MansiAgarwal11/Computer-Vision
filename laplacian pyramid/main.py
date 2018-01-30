#laplacian pyramid

import numpy as np
import cv2

G = cv2.imread('download.jpg')
gpA = [G]
for i in range(3):
    G = cv2.pyrDown(G)
    gpA.append(G)

    
    
# generate Laplacian Pyramid for G
lpA = [gpA[3]]
for i in range(2,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = np.subtract(gpA[i-1],GE) #TODO  #operands could not be broadcast together with shapes (79,161,3) (80,162,3) ????
    lpA.append(L)
    

