import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\feature-matching-template.jpg",0)
img2 = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\feature-matching-image.jpg",0)

orb = cv2.ORB_create()  # using ORB (Oriented FAST and Rotated Brief)

kp1, des1 = orb.detectAndCompute(img1,None)  #key points,descriptor
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)  #sort according to best match to worst match

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2) #10 matches
plt.imshow(img3)
plt.show()
