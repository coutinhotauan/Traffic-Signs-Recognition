import cv2
import numpy as np
import os

for file in os.listdir("new_pos"):
	try:
		file = "new_pos/"+file
		print(file)
		img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
		resized_image = cv2.resize(img, (50, 50))
		cv2.imwrite(file, resized_image)
	except Exception as e:
		print("nao foi possivel converter a imagem"+file+str(e)) 
