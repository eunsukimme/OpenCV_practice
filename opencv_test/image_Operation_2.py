import cv2
import numpy as np

img1 = cv2.imread('logo.png')
img2 = cv2.imread('lena.jpg')

# 삽입할 이미지의 row, col, channel 정보
rows, cols, channels = img1.shape

# 대상 이미지에서 삽입할 이미지의 영역을 추출
roi = img2[0:rows, 0:cols]

# mask를 만들기 위해서 img1을 gray로 변경후 binary image로 전환
# mask는 logo 부분이 흰색(255), 바탕은 검은색(0)
# mask_inv는 logo부분이 검은색(0), 바탕은 흰색(255)

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('1', img2gray)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('2', mask)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('3', mask_inv)

# bitwise_and 연산자는 둘다 0이 아닌 경우만 값을 통과 시킨다.
# 즉 mask가 검정색이 아닌 경우만 통과가 되기 떄문에 mask영역 이외는 모두 제거된다
# 아래 img1_fg의 경우는 bg가 제거 되고 fg(logo부분)만 남게 된다.
# img2_bg는 roi영역에서 logo 부분이 제거되고 bg만 남게된다.
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('4', img1_fg)
cv2.imshow('5', img2_bg)

# 2개의 이미지를 합치면 바탕은 제거되고 logo부분만 합쳐짐.
dst = cv2.add(img1_fg, img2_bg)
cv2.imshow('6', dst)

# 합쳐진 이미지를 원본 이미지에 추가.
img2[0:rows, 0:cols] = dst

cv2.imshow('res', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
