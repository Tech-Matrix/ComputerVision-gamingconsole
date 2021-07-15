import cv2
import numpy as np

img1 = cv2.imread("image.jpg")
img2 = cv2.imread("image2.jpg")
diff = cv2.absdiff(img1, img2)
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

th = 1
imask = mask > th

canvas = np.zeros_like(img2, np.uint8)
canvas[imask] = img2[imask]

cv2.imshow("canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
