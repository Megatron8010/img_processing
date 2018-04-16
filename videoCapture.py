import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()   #cap.read() eturns true if everything is all right
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # to convert to gray
    cv2.imshow('frame',frame)  # natural frame
    cv2.imshow('gray',gray)     #gray frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  #0xFF gotta add it for 64 bit and q to exit
        break
cap.release()  # release the capture 
cv2.destroyAllWindows()
