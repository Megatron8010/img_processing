import numpy as np
import cv2

img= cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\greywatch.png",cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(50,50),(255,0,0),5)  #line(whatpic,(start),(end),(color value in bgr),(optional line width))

cv2.rectangle(img,(15,25),(100,150),(0,200,0),5)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
