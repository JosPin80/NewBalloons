import cv2 as cv
import rescale


imge = cv.imread('read_photo/1695802651_gas-kvas-com-p-kartinki-kot-10.jpg')
img = rescale.rescaleFrame(imge)
cv.imshow('Cat', img)


# Конвертируем в серый фон
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Размытие
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Нахождение краёв
canny = cv.Canny(blur, 125, 160)
cv.imshow('Canny', canny)

# Даменирование изображения
dilated = cv.dilate(canny,(7,7), iterations=3)
cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# размер
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Вырезать из чего либо кусочек Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropping', cropped)

cv.waitKey(0)
