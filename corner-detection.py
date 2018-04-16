import cv2
import numpy as np

img = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\corner-detection.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.15, 10) #shi-tomasi corner detection (number of corner,quality,minimum distance between corners)
corners = np.int0(corners)  #need to convert data type for cv2

for corner in corners:
    x,y = corner.ravel()  #converts n-D aray into 1-D arrays
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('Corner',img)

#finds too many arrays because of antialiasing in image
