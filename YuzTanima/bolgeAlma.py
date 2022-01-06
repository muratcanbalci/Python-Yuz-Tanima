import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"
resim = cv.imread(path+"hababamsinifi.jpg")
cv.rectangle(resim,(260,160),(310,140),[0,0,255],3)
cv.imshow("Hababam Sinifi",resim)
#cv.imwrite(greypath+"yeniresim.jpg",resim)
cv.waitKey(0)
cv.destroyAllWindows()
