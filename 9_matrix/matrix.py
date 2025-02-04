import cv2
import numpy as np

img = cv2.imread("helicopter.jpg", 0)
row, col = img.shape
# print(row, col)

M = np.float32([[1, 0, 10], [0, 1, 70]])

dst = cv2.warpAffine(img, M, (col, row))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()