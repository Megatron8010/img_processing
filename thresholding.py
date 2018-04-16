import cv2
import numpy as np

img = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\bookpage.jpg")

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY) #thresholds to 12 value

grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold2 = cv2.threshold(grayscaled_img,12,255,cv2.THRESH_BINARY) #removes color but has a dark thing in between

th = cv2.adaptiveThreshold(grayscaled_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 61, 2)

cv2.imshow('original',img)
cv2.imshow('grayscaled',threshold2)
cv2.imshow('threshold',threshold)
cv2.imshow('adaptivethreshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()
