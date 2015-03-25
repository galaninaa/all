import cv2
import numpy as np
from matplotlib import pyplot as plt

#img_rgb = cv2.imread('mario.jpg')
marios_coins_Temple= ['black.jpg','black1.jpg','black2.jpg']
template = cv2.imread('coin.jpg',0)
w, h = template.shape[::-1]
i = 1
for img_rgb in marios_coins_Temple:
    img_rgb = cv2.imread(img_rgb,0)
    ret,thresh = cv2.threshold(img_rgb,0,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    try:
        cnt = contours[0]
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        rect = cv2.minAreaRect(cnt)
        bx = cv2.cv.BoxPoints(rect)
        bx = np.int0(bx)
        cv2.drawContours(img_rgb, [bx], 0,(100,100,100),2)
        print "I see smth"
        cv2.imwrite('tmp'+str(i) +'.png',img_rgb)
        i = i + 1
    except:
        print "I see nth"	
    