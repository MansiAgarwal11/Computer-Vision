#gaussian pyramid

import numpy
import cv2



A = cv2.imread('download.jpg')
G = cv2.imread('download.jpg')

gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    cv2.imshow('image',G)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gpA.append(G)
    
    
A = cv2.imread('Chess-Board-Black-White.jpg')

gpA = [A]
for i in range(6):
    A = cv2.pyrUp(A)
    cv2.imshow('image',A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    gpA.append(A)