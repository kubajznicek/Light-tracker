# source bin/activate

import cv2
import numpy as np
import random as rng
import time


SVETLO = 240*3 # Spodni limit pro rozpoznani svetylka R+G+B


rng.seed(12345)
OKNO = 'Kubovo kreslici svetelko'
MAX=768
cv2.namedWindow(OKNO, cv2.WND_PROP_FULLSCREEN)          
#cv2.setWindowProperty(OKNO, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Cela obrazovka
cap = cv2.VideoCapture(0)
_, _ = cap.read()
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)  # nefunguje
cap.set(cv2.CAP_PROP_EXPOSURE, -1.0)  # nefunguje
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cam_x = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_y = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Rozliseni kamery: {}x{}".format(cam_x, cam_y))
print("Expozice: {}".format(cap.get(cv2.CAP_PROP_EXPOSURE)))
page = np.zeros((cam_y, cam_x, 3), dtype=np.uint8)
threshold = 100
time.sleep(1.0)

while(1):

    # Take each frame from camera in BGR
    _, frame = cap.read()

    lower = np.array([SVETLO])
    upper = np.array([MAX])
    frame = np.fliplr(frame) # zrcadli, aby to nebylo stranove prevracene
    scitanec = np.sum(frame, axis=2, keepdims=True) # secti R+G+B 
    mask = cv2.inRange(scitanec, lower, upper)
    # print("Nejsvetlejsi hodnota: {}".format(np.max(mask)))

    # Najdi kontury
    canny_output = cv2.Canny(mask, threshold, MAX+1)     
    contours, _ = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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

    # Kresli caru
    cv2.line(page,bod,bod,(255,0,0),5)

    # Prolni kameru a kresbu
    # res = cv2.bitwise_and(page, frame)
    res = cv2.addWeighted(frame, 0.3, page, 0.7, 0)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow(OKNO,res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('q'):
        break


cv2.destroyAllWindows()


