# source venv/bin/activate
#  v4l2-ctl -d /dev/video0 --set-ctrl=exposure_auto=3

import cv2
import numpy as np
import random as rng
import time

resolution_x = 1280
resolution_y = 720

def menuAkce (bod,barva,tloustka):
    barva,tloustka=menuAkceInteral (bod,barva,tloustka)
    menuAkceInteral (bod,barva,tloustka)
    renderMenu ()
    return barva,tloustka

def menuAkceInteral (bod,barva,tloustka):
    if barva == cerna and tloustka > 3:
      tloustka=tloustka-3
    if bod[1] < 40:
      return cervena,tloustka
    if bod[1] <80:
      return modra,tloustka
    if bod[1] <120:
      return zelena,tloustka
    if bod[1] <160:
      return bila,tloustka
    if bod [1] < 220:
      return cerna,tloustka+3
    if bod [1] > 420:
      return barva,10
    if bod [1] < 420:
      if bod [1] > 375:
        return barva,5
    if bod [1] < 375:
      if bod[1] > 325:
        return barva,2
    if bod [1] > 300:                         # ulozeni z menu
        if bod [1] < 330:
            time.sleep (0.2)
            if bod [1] > 300:
                if bod [1] < 330:
                  cv2.imwrite("Image.jpg", page)
    return barva,tloustka

def renderMenu():
    menu[:] = bila
    vyska = 30
    zacateky = 10
    mezera = 10
    odstup = 40
    odstup2 = 5
    for idx,b in enumerate([cervena,modra,zelena,bila,cerna]):
        cv2.rectangle(menu, (10,zacateky+odstup*idx),(40,odstup*(idx+1)),b,-1)
        cv2.rectangle(menu, (10,zacateky+odstup*idx),(40,odstup*(idx+1)),cerna,1)

    for idx,c in enumerate([10,5,2]):
        cv2.line(menu, (10,450-odstup*idx),(40,450-odstup*idx),barva,thickness=c)

    for idx,d in enumerate (cerna):
        cv2.rectangle(menu,(10,300-odstup*idx),(40,330-odstup*idx),d,2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(menu,'s',(17,351),font,1,cerna,3)

    menu[174:200, 11:41] = guma



SVETLO = 730 # Spodni limit pro rozpoznani svetylka R+G+B

tloustka = 2
cervena = (0,0,255)
modra = (255,0,0)
zelena = (0,255,0)
bila = (255,255,255)
cerna = (0,0,0)
barva = modra
guma = cv2.imread('guma_scale.png',3)

rng.seed(12345)
OKNO = 'Kubovo kreslici svetelko'
MAX=768
cv2.namedWindow(OKNO, cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty(OKNO, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Cela obrazovka
cap = cv2.VideoCapture(0)
_, _ = cap.read()
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)  # nefunguje
cap.set(cv2.CAP_PROP_EXPOSURE, 200)  # nefunguje
cap.set(cv2.CAP_PROP_BRIGHTNESS, 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_y)
cam_x = resolution_x 
cam_y = resolution_y
print("Rozliseni kamery: {}x{}".format(cam_x, cam_y))
print("Expozice: {}".format(cap.get(cv2.CAP_PROP_EXPOSURE)))
page = np.zeros((cam_y, cam_x, 3), dtype=np.uint8)
threshold = 100
time.sleep(1.0)

menu = np.zeros((cam_y, 50, 3), dtype=np.uint8)
renderMenu ()

predchozi = None

while(1):

    # Take each frame from camera in BGR
    err, frame = cap.read()

    lower = np.array([SVETLO])
    upper = np.array([MAX])
    frame = np.fliplr(frame) # zrcadli, aby to nebylo stranove prevracene
    scitanec = np.sum(frame, axis=2, keepdims=True) # secti R+G+B 
    mask = cv2.inRange(scitanec, lower, upper)
    print("Nejsvetlejsi hodnota: {}".format(np.max(scitanec)))
    #print("Expozice: {}".format(cap.get(cv2.CAP_PROP_EXPOSURE)))

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
    if bod == (0,0):
        predchozi = None
    else:
        # Kresli caru
        cv2.line(page,bod,bod,(barva),tloustka)

        if predchozi == None:
            predchozi = bod
        else:
            if bod[0] < 50:
                barva,tloustka=menuAkce(bod,barva,tloustka)
            else:
                cv2.line(page, predchozi, bod,(barva),tloustka)
                predchozi = bod
    page[:,:50]=menu

    # Prolni kameru a kresbu
    res = cv2.addWeighted(frame, 0.5, page, 0.5, 0)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow(OKNO,cv2.resize(res, (1920, 1080)))
    #cv2.imshow(OKNO,res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('q'):
        break
    if k == ord('s'):
        cv2.imwrite("../../../Desktop/Image.jpg", page) # ulozi to i s menu  cesta k souboru
    if k == ord('w'):
        barva = bila
        renderMenu ()
    if k == ord('r'):
        barva = cervena
        renderMenu ()
    if k == ord('b'): #xxxxxxxxxxxxxxxxxxxxxxxxx     pridat zbyle barvy
        barva = modra
        renderMenu ()
    if k == ord('g'):
        barva = zelena
        renderMenu ()
    if k == ord('e'):
        barva = cerna
        renderMenu ()
    if k == ord('1'):
        tloustka = 2
    if k == ord('2'):
        tloustka = 5
    if k == ord('3'):
        tloustka = 10
    if k == ord('c'):
        page = np.zeros((cam_y, cam_x, 3), dtype=np.uint8)
        cv2.rectangle(page,(0,0), (50,480), bila, thickness=-1)
cv2.destroyAllWindows()


