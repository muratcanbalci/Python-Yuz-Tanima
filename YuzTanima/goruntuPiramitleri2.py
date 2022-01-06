import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"

resim = np.zeros((300,300,3),dtype="uint8")
#resim = cv.imread(path+"natalieportman.jpg")

print(resim)

cv.waitKey(0)
cv.destroyAllWindows()