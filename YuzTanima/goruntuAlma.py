import cv2 as cv
import numpy as np

kamera = cv.VideoCapture(0) 
# 0 Dersek direkt bilgisayarımızın kamerasını kullanır.
# 1 Dersek usbye takılı kamera var ise onu kullanır.
# 2 Dersek verilen video adresinden görüntü alabiliriz.

while True:
    ret,goruntu=kamera.read()
    
    cv.imshow("Murat",goruntu)
    
    if cv.waitKey(30) & 0xFF == ('q'):
        break
kamera.release()
cv.destroyAllWindows()