import cv2 as cv
import numpy as np

kamera = cv.VideoCapture(0)

while True:
    ret,goruntu=kamera.read()
    cv.rectangle(goruntu,(100,100),(200,200),(25,36,98),3)
    cv.line(goruntu,(0,0),(100,100),(0,0,255),2)
    cv.circle(goruntu,(150,150),50,(80,150,35),2)
    cv.putText(goruntu,"Murat",(220,200),cv.FONT_HERSHEY_DUPLEX,
               1,(200,0,0),2)    
    cv.imshow("Murat",goruntu)
    
    if cv.waitKey(25) & 0xFF==('Q'):
        break
kamera.release()
cv.destroyAllWindows()        