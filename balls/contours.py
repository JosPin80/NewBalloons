import cv2 as cv
import numpy as np


img = cv.imread('read_photo/kotik_1.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blank, 125, 175)
cv.imshow('Canny Edge', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contours fond')

cv.drawContours(blank, contours, -1, (255, 0, 0), 1)
cv.imshow('Draw', blank)

cv.waitKey(0)
