# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:21:01 2019

@author: bhaik
"""

import cv2
import numpy as np
from scipy import ndimage

kernel_3x3 = np.array([[-1,-1,-1],
                       [-1, 8,-1],
                       [-1,-1,-1]])

kernel_5x5 = np.array([[[-1,-1,-1,-1,-1],
                       [-1, 1, 2, 1,-1],
                       [-1, 2, 4, 2,-1],
                       [-1, 1, 2, 1,-1],
                       [-1,-1,-1,-1,-1]],
                      [[-1,-1,-1,-1,-1],
                       [-1, 1, 2, 1,-1],
                       [-1, 2, 4, 2,-1],
                       [-1, 1, 2, 1,-1],
                       [-1,-1,-1,-1,-1]],
                       [[-1,-1,-1,-1,-1],
                       [-1, 1, 2, 1,-1],
                       [-1, 2, 4, 2,-1],
                       [-1, 1, 2, 1,-1],
                       [-1,-1,-1,-1,-1]]])

#imgpath = "E:\\opencv python\\images 2\\misc\\4.2.06.tiff"

cap = cv2.VideoCapture(1)

while True:
    
    ret, frame = cap.read()
    
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
    #image = cv2.resize(image,(1280,720),interpolation = cv2.INTER_CUBIC)
    k3 = ndimage.convolve(grayImage, kernel_3x3)
    #k5 = ndimage.convolve(frame, kernel_5x5)

    blurred = cv2.GaussianBlur(frame, (17,17), 0)
    g_hpf = frame - blurred
    
    n = k3/255
    
    #print(n[0][0])
    r = int(n[0][0])
    
    print(r)
    
    #if n.all>0.5:
    #    print("1")
    #else:
    #    print("0")
    
    #cv2.imshow("3x3", k3)
    #cv2.imshow("5x5", k5)
    #cv2.imshow("g_hpf", g_hpf)
    cv2.imshow("img", k3)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()

