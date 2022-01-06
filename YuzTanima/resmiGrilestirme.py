import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"
resim = cv.imread(path+"natalieportman.jpg")
resimGri=cv.cvtColor(resim,cv.COLOR_BGR2GRAY)

cv.imshow("Orjinal",resim)
cv.imshow("Grilestirilmis",resimGri)

orjinalYukseklik,orjinalGenislik,orjinalKanal = resim.shape
griYukseklik,griGenislik = resimGri.shape

print("Orjinal: ",orjinalYukseklik,orjinalGenislik,orjinalKanal)
print("Gri resim: ",griYukseklik,griGenislik)

cv.waitKey(0)
cv.destroyAllWindows()