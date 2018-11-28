import numpy as np
import cv2 as cv


fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('out.avi', fourcc, 20.0, (640, 480))
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    out.write(frame)
    cv.imshow("video", frame)
    c = cv.waitKey(10)
    print(c)
    if c == 27:
        break
cap.release()
out.release()
cv.destroyAllWindows()