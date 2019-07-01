# -*- coding: utf-8 -*-

# 트랙바와 OpenCV 연동 방법에 대해서 알 수 있다
# cv2.getTrackbarPos(), cv2.createTrackbar() 함수에 대해서 알 수 있다

### Demo
# cv2.createTrackbar(트랙바 이름, 윈도우 이름, 트랙바 초기값, 트랙바 최대값, 값이 변경될 때 실행되는 콜백함수)
# cv2.getTrackbarPos(트랙바 이름, 트랙바가 등록된 윈도우 이름)

import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# 트랙바를 생성하여 namedWindow에 등록
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0:OFF\n1:0\n'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while(1):
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0 # 모든 행/열 좌표값을 0으로 변경 => 검은색
    else:
        img[:] = [b, g, r] # 모든 행/열 좌표값을 [b, g, r]로 변경

cv2.destroyAllWindows()