import cv2
import numpy as np

img = cv2.imread("j.png", 0)
img1 = cv2.imread("opening.png",0)
img2 = cv2.imread("closing.png",0)
img = cv2.resize(img, (200, 400))
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Img", img)
cv2.imshow("Img1", img1)
cv2.imshow("Img2", img2)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradient", gradient)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
