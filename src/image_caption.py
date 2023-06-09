import cv2
import time

cap = cv2.VideoCapture('C:\\Users\\mvideo\\Desktop\\Practice2_ImageCapture\\resources\\cam_video.mp4')
leftCounter = 0
rightCounter = 0
flag=None


while (True) :
    ret, frame = cap.read()
    if not ret:
        break

    # Переход в чернобелый формат
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

    # Выполнение анализа кадра
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        c = max(contours, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)

        if x + w // 2 > 320:
            rightCounter += 0 if flag else 1
            color = (255, 0, 0)
            flag = True
        else:
            leftCounter += 1 if flag else 0
            color = (0, 0, 255)
            flag = False

        cv2.putText(frame, "left: " + str(leftCounter) + " right: " + str(rightCounter), (0, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    cv2.imshow('video with rectangle', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)


cap.release()
cv2.destroyAllWindows()
