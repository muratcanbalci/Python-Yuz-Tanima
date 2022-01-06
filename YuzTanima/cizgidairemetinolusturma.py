import cv2 as cv
import numpy as np

resim=np.zeros((300,300,3),dtype="uint8")

cv.line(resim,(0,0),(100,100),(20,60,255),3)
cv.circle(resim,(150,150),25,(0,255,0),2)
cv.putText(resim,"Merhaba",(100,200),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)

cv.imshow("deneme",resim)
cv.waitKey(0)
cv.destroyAllWindows()