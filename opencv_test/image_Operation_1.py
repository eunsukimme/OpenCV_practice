import cv2
import numpy as np

# Saturation 연산시 한계값 초과는 한계값으로 설정한다.
# modulo 연산은 결과가 256보다 크면 256으로 나눈 나머지 값으로 결정한다.

img1 = cv2.imread('flower1.jpg')
img2 = cv2.imread('flower2.jpg')

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing)

while True:
    w = cv2.getTrackbarPos('W', 'image')

    dst = cv2.addWeighted(img1, float(100-w) * 0.01, img2, float(w) * 0.01, 0)

    cv2.imshow('dst', dst)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyALlWindows()
