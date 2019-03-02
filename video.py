import cv2
import numpy as np
import pafy # pip3 install youtube-dl

url = "https://www.youtube.com/watch?v=bjzkmHRLTaI"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

#captura = cv2.VideoCapture('drone.mp4')                 # Video File
#captura = cv2.VideoCapture(0)                           # Webcam 1,2,3
#captura = cv2.VideoCapture('http://192.168.1.68:8081/') # IPCamara

captura = cv2.VideoCapture() #Youtube
captura.open(best.url)

while True:
    ret, frame = captura.read()


    
    cv2.imshow('Salida',frame)
    k = cv2.waitKey(24)&0xFF
    if k == 27:
        break
    
captura.release()
cv2.destroyAllWindows()
