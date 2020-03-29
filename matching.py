# source bin/activate

import cv2
import numpy as np
import random as rng
import time


SVETLO = 760 # Spodni limit pro rozpoznani svetylka R+G+B

tloustka = 2
cervna = (0,0,255)
modra = (255,0,0)
zelena = (0,255,0)
barva = modra

rng.seed(12345)
OKNO = 'Kubovo kreslici svetelko'
MAX=768
cv2.namedWindow(OKNO, cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty(OKNO, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Cela obrazovka
cap = cv2.VideoCapture(0)
_, _ = cap.read()
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)  # funguje
cap.set(cv2.CAP_PROP_EXPOSURE, 300)  # funguje
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam_x = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_y = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Rozliseni kamery: {}x{}".format(cam_x, cam_y))
print("Expozice: {}".format(cap.get(cv2.CAP_PROP_EXPOSURE)))
page = np.zeros((cam_y, cam_x, 3), dtype=np.uint8)
threshold = 100
time.sleep(1.0)

cv2.line(page,(50, 0),(50, 250),(255, 255, 255),100)
predchozi = None


template = cv2.imread('pes.jpg',0)
w, h = template.shape[::-1]
while(1):

    # Take each frame from camera in BGR
    err, frame = cap.read()
    print (type(frame))
    #frame = np.fliplr(frame)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grey,template,cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = min_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(res,top_left, bottom_right, 255, 2)
    cv2.imshow(OKNO,res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('q'):
        break