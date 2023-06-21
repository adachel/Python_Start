import cv2

img = cv2.imread('D:/Works/IT/Python_Start/OpenCV/test.jpg')
print(img.shape) # показывает размер картинки оригинал
#img = cv2.resize(img, (500, 500))
#print(img.shape) # после изменения
#print(img)
cv2.imshow('Resalt', img) # показать картинку

cv2.waitKey(0) # окно с картинкой закроется через милисек в скобках
