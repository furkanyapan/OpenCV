import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((500, 500), np.uint8) + 50

# cv2.rectangle(img, (0, 60), (200, 150), (255, 255, 255), -1)
# cv2.rectangle(img, (200, 170), (350, 200), (255, 255, 255), -1)

img = cv2.imread("smile.jpg")


plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("Img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
