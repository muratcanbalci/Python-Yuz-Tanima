# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:53:31 2021

@author: Murat Can BALCI
"""
import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"
resim2 = cv.imread(path+"turkansoray.jpg")
resim1 = cv.imread(path+"emelsayin.jpg")

print(resim1[100,200])
print(resim2[300,430])

cv.imshow("Emel SAYIN",resim1)
cv.imshow("Turkan SORAY",resim2)

print(resim1[100,200]+resim2[300,430])

cv.waitKey(0)
cv.destroyAllWindows()