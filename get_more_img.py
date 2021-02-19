import urllib.request
import cv2
import numpy as np
import os

images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03673027'
image_urls = urllib.request.urlopen(images_link).read().decode()
pic_num = 185

if not os.path.exists('negatives_validation'):
    os.makedirs('negatives_validation')

for i in image_urls.split('\n'):
    try:
        urllib.request.urlretrieve(
            i, "negatives_validation/"+"neg"+str(pic_num)+".jpg")
        #img = cv2.imread("validation/"+str(pic_num)+".jpg", cv2.IMREAD_GRAYSCALE)
        # should be larger than samples / pos pic (so we can place our image on it)
        #resized_image = cv2.resize(img, (100, 100))
        #cv2.imwrite("neg/"+str(pic_num)+".jpg", resized_image)
        pic_num += 1

    except Exception as e:
        print(str(e))
