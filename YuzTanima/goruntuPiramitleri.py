import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"

resim = cv.imread(path+"natalieportman.jpg")

ikiKatBuyuk = cv.pyrUp(resim)
ikiKatKucuk = cv.pyrDown(resim)

print("Orjinal resim",resim.shape)
print("İki kat buyuk resim",ikiKatBuyuk.shape)
print("İki kat kucuk resim",ikiKatKucuk.shape)

cv.imshow("Orjinal",resim)
cv.imshow("Iki kat buyuk",ikiKatBuyuk)
cv.imshow("Iki kat kucuk",ikiKatKucuk)

cv.waitKey(0)
cv.destroyAllWindows()