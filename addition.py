import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\3D-Matplotlib.png")
img2 = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\mainsvmimage.png")

#add = img1 + img2 to add without any opacity

weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)  #last value is gamma value



cv2.imshow('add',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
