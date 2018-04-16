import cv2
import numpy as np

img_rgb = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\mario.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\mariocoin.jpg",0) #0 for gray scale
w,h = template.shape[::-1] #width , height from the image

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.99
loc = np.where( res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w ,pt[1]+h),(0,0,255),2)
    
cv2.imshow('Detected',img_rgb)
    
