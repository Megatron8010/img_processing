import numpy as np
import cv2

img = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\greywatch.png",cv2.IMREAD_COLOR)
px = img[55,55]
img[55,55] = [0,255,0] # acessing and editing single pixel value

# img[100:150,100:150] = [255,0,0] editing region of an image

watch_face = img[35:100,110:200]
img[0:65,0:90] = watch_face   #kind of cropping

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
