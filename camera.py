# source bin/activate

import cv2
import numpy as np
import random as rng

rng.seed(12345)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(cv2.CAP_PROP_EXPOSURE, 10.0)
print (cap.get(cv2.CAP_PROP_EXPOSURE ))
threshold = 100
_, res = cap.read()

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower = np.array([254,254,254])
    upper = np.array([255,255,255])
    lower2 = np.array([2])
    upper2 = np.array([255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower, upper)
    mask = cv2.blur(mask, (10, 10))
    mask = cv2.inRange(mask, lower2, upper2)

    # Detect edges using Canny
    canny_output = cv2.Canny(mask, threshold, threshold * 2)     

    # Find contours
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Approximate contours to polygons + get bounding rects and circles
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)

    r = 0
    c = [0, 0]
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

    for i in range(len(contours)): 
        
        if radius[i] > r:
            r = radius[i]
            c = centers[i]
    
    bod =  (int(c[0]), int(c[1]))  

    # Draw polygonal contour + bonding rects + circles
    cv2.line(res,bod,bod,(255,0,0),5)
    #cv2.circle(res, (int(c[0]), int(c[1])), 3, (200, 199, 9), CV_FILLED, 8,0)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()


