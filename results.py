import cv2
import numpy as np
import os

sign_cascade = cv2.CascadeClassifier("data/cascade.xml")
pos = 0
neg = 0
i = 0
j = 0

for file in os.listdir("positives_validation"):
    name = str(file)
    img = cv2.imread("positives_validation/"+str(name))
    i += 1

    img = cv2.resize(img, (100, 100))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    traffic_signs = sign_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in traffic_signs:
        pos += 1
        break


for file in os.listdir("negatives_validation"):
    name = str(file)
    img = cv2.imread("negatives_validation/"+str(name))
    j += 1

    img = cv2.resize(img, (100, 100))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    traffic_signs = sign_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in traffic_signs:
        neg += 1
        break

# recall = classificações corretas/quantidade da classe
recall = pos / i

# precision = classificações corretas/quantidade classificada
precision = pos / (pos + neg)

# verdadeiro-negativo
vn = j - neg

# falso negativo
fn = i - pos

acuracia = (pos + vn)/(pos + vn + neg + fn)

print("||===================================||")
print("||              IMAGENS              ||")
print("||imagens negativas: " + str(j) + "            ||")
print("||imagens positivas: " + str(i) + "            ||")
print("||total: " + str(i+j) + "                        ||")
print("|| --------------------------------- ||")
print("||             RESULTADOS            ||")
print("||objetos detectados: " + str(pos+neg) + "           ||")
print("||verdadeiros-positivos: " + str(pos) + "        ||")
print("||falsos-positivos: " + str(neg) + "               ||")
print("||verdadeiros-negativos: " + str(vn) + "        ||")
print("||falsos-negativos: " + str(fn) + "               ||")
print("|| --------------------------------- ||")
print("||               ÍNDICES             ||")
print("||recall: {:.5f}                    ||".format(recall))
print("||precision: {:.5f}                 ||".format(precision))
print("||acuracia: {:.5f}                  ||".format(acuracia))
print("||===================================||")
