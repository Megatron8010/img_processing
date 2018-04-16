import cv2
import numpy as np

img = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\images\maxresdefault.jpg")

frame = img
hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hue sat value

lower_red = np.array([168,0,0])
upper_red = np.array([188,255,255])

mask = cv2.inRange(hsv,lower_red,upper_red)  #evrything in range is white or else black
res = cv2.bitwise_and(frame,frame,mask= mask)  # where there is 1(white) in the mask we will show the colour in the frame



cv2.imshow("image",img)
cv2.imshow("imagehsv",hsv)
cv2.imshow("imagemask",mask)
cv2.imshow("imageres",res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  this is how you convert bgr to hsv need to reverse the value in uint8
##>>> red = np.uint8([[[168,57,63]]])
##>>> hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
##>>> hsv_red

