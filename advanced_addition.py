import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\3D-Matplotlib.png")
img2 = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\mainlogo.png")

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) #anything below 220 is black and above is white
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('add',img2)
cv2.imshow('add2',mask)
cv2.imshow('add3',mask_inv)

cv2.imshow('addroi',roi)
cv2.imshow('add4',img1_bg)
cv2.imshow('add5',img2_fg)
cv2.imshow('add6',dst)
cv2.imshow('add7',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
