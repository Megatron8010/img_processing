import numpy as np
import cv2

cap = cv2.VideoCapture(r"C:\Users\rajsi\Documents\img_processing\videos\people-walking.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()  #foreground background

while True:
    ret,frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow("original",frame)
    cv2.imshow("fg",fgmask)

    k = cv2.waitKey(30) & 0xff
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()

#can use morphological transformation for noise reduction
