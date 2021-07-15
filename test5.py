import cv2
import numpy as np
import pyautogui
import time

time.sleep(5)
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
frame1 = cv2.flip(frame1, 1)
frame2 = cv2.flip(frame2, 1)
x = 0
y = 0
x1 = 0
flag = 0
y1 = 0
# pyautogui.mouseDown()
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    faces = face_cascade.detectMultiScale(frame1, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    if flag is 0:
        x1 = x
        y1 = y
        flag = 1
    if((x1-x) > 20 and abs(y1-y) < 10):
        print("right")
        # x1 = x
        # y1 = y

        pyautogui.keyUp('left')
        pyautogui.keyDown('right')
    elif((x1-x) < -20 and abs(y1-y) < 10):
        print("left")
        # x1 = x
        # y1 = y
        pyautogui.keyUp('right')
        pyautogui.keyDown('left')
    elif((y1-y) > 10):
        print("up"+str(y1-y))
        # x1 = x
        # y1 = y
        pyautogui.keyUp('down')
        pyautogui.keyDown('up')

    elif((y1-y) < -10):
        print("down"+str(y1-y))
        # x1 = x
        # y1 = y
        pyautogui.keyUp('up')
        pyautogui.keyDown('down')

    else:
        pyautogui.keyUp('down')
        pyautogui.keyUp('up')
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')
    cv2.imshow("FEED", frame1)
    frame1 = frame2
    _, frame2 = cap.read()
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()
