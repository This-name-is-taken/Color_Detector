import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

yellow_lower = np.array([22, 99, 79])
#yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([42, 255, 255])
prev_y = 0

while True:
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    for c in contours:
        area = cv2.contourArea(c)
        #print(area)
        if area > 3000:
            #print(area)
            #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255, 0), 2)
            if y < prev_y:
                print('moving_down')
                #pyautogui.press('space')
            else:
                print('doing_nothing')
            prev_y = y

    #cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
