# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 디지털 영상의 표현 방법에 대해서 알 수 있다
# Color-space 중 Binary Image, Grayscale, RGB, HSV에 대해서 알 수 있다
# Color-space 변환 방법에 대해서 알 수 있다
# 동영상에서 간단한 Object Tracking을 할 수 있다
# cv2.cvtColor(), cv2.inRange() 함수에 대해서 알 수 있다

### Color-space 변환
# cv2.cvtColor(이미지, 변환 코드)
# BGR-> Grayscale : cv2.COLOR_BGR2GRAY
# BGR-> HSV : cv2.COLOR_BGR2HSV

### Object Tracking
# 영상에서 파란색 부분을 찾아서 binary image로 보여준다. 다음과 같은 과정으로 구현한다
# 1. Video로 부터 Frame을 읽어들인다
# 2. frame을 HSV로 변환한다
# 3. 변환한 이미지에서 blue영역을 찾아서 mask를 생성한다
# 4. frame에 mask를 적용하여 이미지를 보여준다

# Camera 객체를 생성한 후 사이즈를 320 X 240 으로 조정한다
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while(1):
    # camera에서 frame을 capture 한다
    ret, frame = cap.read()

    if ret:
        # BGR-> HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue 영역의 from - to
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # 이미지에서 blue영역 mask 검출
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # bit 연산자를 통해서 blue 영역만 남김
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == 27 :
        break

cap.release()
cv2.destroyAllWindows()