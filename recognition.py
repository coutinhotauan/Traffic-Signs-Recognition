import cv2
import numpy as np
import os

sign_cascade = cv2.CascadeClassifier("data/cascade.xml")
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i = 0

for file in os.listdir("test_images"):
    name = str(file)
    img = cv2.imread("test_images/"+str(name))

    img = cv2.resize(img, (100, 100))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    traffic_signs = sign_cascade.detectMultiScale(gray, 1.3, 5)  

    for (x, y, w, h) in traffic_signs:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    img = cv2.resize(img, (300, 300))
    name_window = "image" + str(i)
    i += 1
    cv2.imshow(name_window, img)

cv2.waitKey(0)
cv2.destroyAllWindows()

