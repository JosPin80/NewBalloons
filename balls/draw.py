import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Нарисовать объект на окне
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Red', blank)

# 2. Нарисуем пустой Прямоугольник
# cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)
#
# # 3. Нарисуем круг
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 250, (0, 0, 255), thickness=3)
# cv.imshow('Circle', blank)

# 4. Нарисуем линию
# cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=4)
# cv.imshow('Line', blank)

# 5. Напишем текст
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
