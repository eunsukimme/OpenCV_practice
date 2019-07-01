# -*- coding: utf-8 -*-

# 이미지의 더하기, 빼기, 비트 연산에 대해서 알 수 있다
# cv2.add(), cv2.addWeighted() 함수에 대해서 알 수 있다
import cv2
import numpy as np

### 이미지 더하기
# 이미지를 더하는 방법은 OpenCV의 cv2.add() 함수를 사용하는 방법과
# Numpy 연산, 즉 img1 + img2로 하는 방법이 있다. 둘 다 더하는 것은 같지만 결과는 다르게 나타난다
# OpenCV의 cv2.add() 는 Saturation 연산을, Numpy는 modulo 연산을 한다

# Saturation 연산은 한계값을 정하고 그 값을 벗어나는 경우 모두 특정 값으로 계산하는 방식이다
# 이미지에서 0 이하는 모두 0, 255 이상은 모두 255로 표현하는 것이다
# Modulo 연산은 a와 b는 n으로 나눈 나머지 값이 같다는 의미이다
# 시계를 예로 들면 2와 14는 12로 나눈 나머지가 2로 동일하다
# 이미지에선 연산의 결과가 256보다 큰 경우는 256으로 나눈 나머지 값으로 결정을 한다

img1 = cv2.imread('flower1.jpg')  # 이미지를 컬러로 읽어들인다(투명 무시)
img2 = cv2.imread('flower2.jpg')
addImg = cv2.add(img1, img2)

cv2.imshow('addImg', addImg)
cv2.waitKey(0)

addImg2 = np.add(img1, img2)

cv2.imshow('addImg2', addImg2)
cv2.waitKey(0)
cv2.destroyAllWindows()

### 이미지 Blending
# 이미지를 서로 합칠 때 가중치를 두어 합치는 방법

def nothing(x):
    pass


cv2.namedWindow('image')
cv2.resizeWindow('image', 400, 400)
cv2.createTrackbar('W', 'image', 0, 100, nothing)

while(True):
    w = cv2.getTrackbarPos('W', 'image')

    dst = cv2.addWeighted(img1, float(100-w) * 0.01, img2, float(w) * 0.01, 0)

    cv2.imshow('dst', dst)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cv2.destroyAllWindows()


### 비트 연산
# 비트 연산은 AND, OR, NOT, XOR 연산을 말한다
# 비트연산은 이미지에서 특정 영역을 추출할 때 유용하게 사용된다
# 예를 들면 이미지에서 바탕을 제거하고, 2개의 이미지를 합치는 경우이다
# 아래는 OpenCV 로고에서 바탕을 제거하고, 이미지에 추가하는 예제이다

logo = cv2.imread('logo.png')
lena = cv2.imread('lena.jpg')

# 삽입할 이미지의 행, 열, 채널 정보
rows, cols, channels = logo.shape

# 대상 이미지에서 삽입할 이미지의 영역을 추출
roi = lena[0:rows, 0:cols]

# mask를 만들기 위해서 logo를 그레이 스케일로 변경 후 binary image로 전환
# mask는 logo 부분이 흰색(255), 바탕은 검정색(0)
# mask_inv는 logo부분이 검은색(0), 바탕은 흰색(255)
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# bitwise_and 연산자는 둘 다 0이 아닌 경우만 값을 통과시킴
# 즉, mask가 검정색이 아닌 경우만 통과되기 때문에 mask영역 이외는 모두 제거됨
# 아래 logo_fg의 경우 bg가 제거되고 fg(logo부분)만 남게됨
# lena_bg는 roi영역에서 logo부분이 제거되고 bg만 남게됨
logo_fg = cv2.bitwise_and(logo, logo, mask=mask)
lena_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

cv2.imshow('logo_fg', logo_fg)
cv2.imshow('lena_bg', lena_bg)
cv2.waitKey(0)

# 2개의 이미지를 합치면 바탕은 제거되고 로고 부분만 합쳐진다
dst = cv2.add(logo_fg, lena_bg)

# 합쳐진 이미지를 원본 이미지에 추가
lena[0:rows, 0:cols] = dst

cv2.imshow('result', lena)
cv2.waitKey(0)
cv2.destroyAllWindows()