import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img=cv2.imread('lena.jpg')

cv2.imshow('img',img)
cv2.waitKey()