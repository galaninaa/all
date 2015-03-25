import cv2
import numpy as np
from matplotlib import pyplot as plt

#img_rgb = cv2.imread('mario.jpg')
marios_coins_Temple= ['mario.jpg','mario2.jpg','mario3.jpg','mario4.jpg']
template = cv2.imread('coin.jpg',0)
w, h = template.shape[::-1]
i = 1
for img_rgb in marios_coins_Temple:
    img_rgb = cv2.imread(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        print pt
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)        
    cv2.imwrite('res'+str(i) +'.png',img_rgb)
    i = i + 1