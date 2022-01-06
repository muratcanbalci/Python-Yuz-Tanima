# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:05:17 2021

@author: Murat Can BALCI
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:53:31 2021

@author: Murat Can BALCI
"""
import cv2 as cv
import numpy as np

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
greypath = "D:\\PROJELER\\Python\\YuzTanima\\greyphotos\\"
resim1 = cv.imread(path+"cemyilmaz.jpg")
resim2 = cv.imread(path+"ozanguven.jpg")

toplam=cv.add(resim1,resim2)
agirlikliToplama=cv.addWeighted(resim1,0.7,resim2,0.3,0)
cv.imshow("Toplanmis Resimler", toplam)
cv.imshow("Agirlikli Toplam",agirlikliToplama)
cv.waitKey(0)
cv.destroyAllWindows()