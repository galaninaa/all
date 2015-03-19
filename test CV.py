#http://docs.opencv.org/trunk/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#http://answers.opencv.org/question/44783/saving-video-from-webam-stream-no-file-created/

import cv2 as cv
import numpy as nm
#from nxt.locator import find_one_brick
#from nxt.motor import *
 
cap = cv.VideoCapture(0)
fourcc = cv.cv.CV_FOURCC('X','V','I','D')
out= cv.VideoWriter('D:\\output1.avi',fourcc,20.0,(1280,1024),1)
#while(True):
#    # Capture frame-by-frame
#    ret, frame = cap.read()
#    # Our operations on the frame come here
#    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)TypeError: an integer is required
#    # Display the resulting frame
#    cv.imshow('frame',gray)
#    if cv.waitKey(1) & 0xFF == ord('q'):
#        break
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


# When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()