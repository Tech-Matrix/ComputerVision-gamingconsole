import cv2
import numpy as np
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
x1 = 0
y1 = 0
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    # faces = face_cascade.detectMultiScale(frame1, 1.1, 4)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # # Display
    # cv2.imshow('img', frame1)
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 30700:
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'),
                        (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            if((x1-x) > 0 and abs(y1-y)<10):
                print("right")
                x1 = x
                y1 = y
            elif((x1-x) < 0 and abs(y1-y)<10):
                print("left")
                x1 = x
                y1 = y
            if(abs(y1-y)>10):
                print("up/down"+str(y1-y))
                x1 = x
                y1 = y
    cv2.imshow("FEED", frame1)
    frame1 = frame2
    _, frame2 = cap.read()
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
