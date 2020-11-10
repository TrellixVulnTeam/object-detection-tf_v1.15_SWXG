import requests
import cv2
import numpy as np

url = "http://192.168.0.2:8080/shot.jpg"

while True:
    imagen = requests.get(url)
    imagen_array = np.array(bytearray(imagen.content),dtype=np.uint8)
    img = cv2.imdecode(imagen_array,1)
    cv2.imshow('object detection', cv2.resize(img, (800, 600)))

    key = cv2.waitKey(1)
    if key==27:
        break
