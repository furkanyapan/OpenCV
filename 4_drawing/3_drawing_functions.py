import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255
# print(canvas)

# line
# cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)
cv2.line(canvas, (50, 50), (512, 512), (255, 0, 0), 5)
cv2.line(canvas, (100, 50), (100, 250), (0, 0, 255), thickness=7)

# rectangle
cv2.rectangle(canvas, (20, 20), (50, 50), (0, 255, 0), thickness=-1)
cv2.rectangle(canvas, (50, 50), (150, 150), (0, 255, 0), thickness=2)

# circle
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=5)
cv2.circle(canvas, (450, 450), 50, (0, 0, 255), thickness=-1)

# triangle
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

cv2.line(canvas, p1, p2, (0, 0, 0), 4)
cv2.line(canvas, p2, p3, (0, 0, 0), 4)
cv2.line(canvas, p1, p3, (0, 0, 0), 4)

# polylines
points = np.array([[110, 200], [330, 200], [290, 220], [100, 250]], np.int32)
cv2.polylines(canvas, [points], True, (0, 0, 100), 5)

# ellipse
cv2.ellipse(canvas, (350, 350), (80, 20), 10, 90, 360, (255, 255, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
