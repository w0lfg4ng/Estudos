import cv2 as cv

img = cv.imread('fotos\cat.jpg')

cv.imshow('cat', img) #JANELA

cv.waitKey(0) #DELAY