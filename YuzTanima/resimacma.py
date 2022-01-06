import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"
resim = cv.imread(path+"kusresmi.jpg")
cv.imshow("Murat Can",resim)
#cv.imwrite(greypath+"yeniresim.jpg",resim)
cv.waitKey(0)
cv.destroyAllWindows()
