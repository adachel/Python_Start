import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # подгружаем библиотеку

# img = cv2.imread("D:/Works/IT/Python_Start/OpenCV/My.jpg") # берем картинку
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # делаем картинку чернобелой

# faces = face_cascades.detectMultiScale(img_gray) # пердаем сюда серую картинку и определяем лицо

# for(x, y, w, h) in faces: # перебираем лица
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) # делаем рамку

# cv2.imshow("result", img)


# cv2.waitKey(0)

cap = cv2.VideoCapture(0) # для камеры

while True:
    success, frame = cap.read() # получили текущий кадр
    #cv2.imshow("camera", frame) # Выводим на экран
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # делаем картинку чернобелой
    faces = face_cascades.detectMultiScale(img_gray) # пердаем сюда серую картинку и определяем лицо
    
    for(x, y, w, h) in faces: # перебираем лица
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # делаем рамку
        
    cv2.imshow("result", frame)    
    
    if cv2.waitKey(1) & 0xff == ord("q"): # кадр обновляется через 1 миллисек. "q" закрыть окно
        break # выход из цикла while
