import cv2

face_cascade = cv2.CascadeClassifier('trainTest.xml')

image = cv2.VideoCapture(0)
while True:
    ret, frame = image.read()
    if ret == False:
        break
    cv2.imshow("before", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(5, 5),
        flags=0
    )
    for (x, y, w, h) in faces:
        cv2.circle(frame, (int((x + x + w) / 2), int((y + y + h) / 2)), int(w / 2), (0, 0, 255), 2)
        print(len(faces))
        print("x={0}, y={1}, w={2}, h={3}".format(x, y, w, h))
    cv2.imshow("result", frame)
    c = cv2.waitKey(40)
    if c == 27:
        break
