import cv2 as cv

path = "D:\\PROJELER\\Python\\YuzTanima\\photos\\"
image = cv.imread(path+"kusresmi.jpg")

meanFilter = cv.blur(image,(5,5))
medianFilter = cv.medianBlur(image,3)
gauss = cv.GaussianBlur(image,(3,3),0)


cv.imshow("orjinal resim",image)
cv.imshow("mean filter",meanFilter)
cv.imshow("median filter",medianFilter)
cv.imshow("gauss filter",gauss)

cv.waitKey(0)
cv.destroyAllWindows()