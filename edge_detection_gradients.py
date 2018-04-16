import cv2
import numpy as np

img = cv2.imread(r"C:\Users\rajsi\Documents\img_processing\sudoku.jpg")
frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

laplace = cv2.Laplacian(frame,cv2.CV_64F)
sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=1)
sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=1)


cv2.imshow("frame",frame)
cv2.imshow("laplacian",laplace)
cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
