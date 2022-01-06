import cv2 as cv

face_cascade = cv.CascadeClassifier(
    r"D:\PROJELER\Python\YuzTanima\classifier\haarcascade_frontalface_default.xml")

img = cv.imread(r"D:\PROJELER\Python\YuzTanima\photos\muratcan.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

faces = face_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()