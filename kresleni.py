import cv2
import numpy as np
import math
import time


def kruznice( vyska, sirka, x, y, barva ):
  for stupne in range (0, 360):
    pozice=y-math.sin(math.radians(stupne))*vyska
    pozicesirka=x-math.cos(math.radians(stupne))*sirka
    image [int(pozice) , int(pozicesirka)]=barva


for posun in range(0,100):
  # Make empty black image
  image=np.zeros((500,700,3),np.uint8)
  # Define colors
  red = [0,0,255]
  white = [255,255,255]
  brown = [153,184,225]
  #hlava
  kruznice(110, 100, 350+posun, 250, brown)


  #oci
  kruznice(15, 15, 315+posun, 200, white)
  kruznice(15, 15, 385+posun, 200,white)

  

  #nos
  kruznice(25, 15, 350+posun, 250,brown)
  
  #pusa
  for stupne in range (180, 360):
    y=290-math.sin(math.radians(stupne))*30
    x=posun+350-math.cos(math.radians(stupne))*45
    image [int(y) , int(x)]=red

  #vlasy
  for stupne in range (30, 150, 5):
    y=250-math.sin(math.radians(stupne))*110
    x=posun+350-math.cos(math.radians(stupne))*100
    y1=250-math.sin(math.radians(stupne))*150
    x1=posun+350-math.cos(math.radians(stupne))*150
    cv2.line(image, (int(x), int(y)),(int(x1), int(y1)),white)







  # Show image
  cv2.imshow('Kubovo obrazek',image)
  cv2.waitKey(0)




#for pokus in range (stupne)

# Draw a point
#image[10,5]=white
#image[10,6]=white
#for ssssss in range(0, 100):

#for usecka in range(0, 100):
  #  x=usecka
  #  y=250-usecka/2
  #  image[int(y) , int(x)]=white

#for stupne in range (0, 360):
 # y=250-math.sin(math.radians(stupne))*100
 # x=250-math.cos(math.radians(stupne))*100
 # image [int(y) , int(x)]=white
