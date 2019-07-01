# -*- coding: utf-8 -*-

# 개별 픽셀에 접근하고, 수정할 수 있다
# 이미지의 기본 속성을 확인할 수 있다
# 이미지의 ROI(Region of Image)를 설정할 수 있다
# 이미지를 분리하고, 합칠 수 있다
import cv2
import numpy as np

### 픽셀 값(Pixel Value)
# 일반적으로 이미지를 load하면 3차원 행렬 형태로 생성이 된다
# (100, 300, 3) 이러한 형태로 (행, 열, 색정보)를 의미한다
img = cv2.imread('lena.jpg')

# 위와 같이 로드한 후 특정 pixel 값에 접근하려면 다음과 같이 할 수 있다
px = img[100, 200]
print(px) # [24 17 30]
# 즉 100행 200열의 색 값이 24(B), 17(G), 30(R)인 것을 확인할 수 있다
# 만약 B 값만 확인하고 싶을 경우 다음과 같이 할 수 있다
b = img[100, 200, 0]
print(b) # 24

# 이미지 배열의 세 번째 Array에서 0은 B, 1은 G, 2는 R을 의미한다
# 특정 픽셀의 색을 다음과 같이 변경할 수 도 있다
img[100, 200] = [255, 255, 255]  # 100행 200열 픽셀을 흰 색으로 변경

# 일반적으로 특정 픽셀 값을 변경하기 위해선 아래와 같이 사용한다(Numpy 사용)
print(img.item(10, 10, 2)) # (10, 10)의 Red 값 => 59
img.itemset((10, 10, 2), 100) # (10, 10)의 Red값을 100으로 변경
print(img.item(10, 10, 2)) # 100


### 이미지의 기본 속성
# 이미지를 로드 한 후 해당 이미지의 기본적인 정보를 확인해야 한다
# 행과 열의 갯수가 몇개인지, 몇 개의 채널로 구성이 되어있는지가 기본이다
# 이를 확인하기 위해서 img.shape 를 사용하여 튜플 형태로 (행, 열, channel)정보를 리턴한다
print(img.shape) # (255, 400, 3)

# 전체 pixel 수의 확인은 img.size로 확인 가능하다
print(img.size) # 270000

# 이미지의 Datatype은 img.dtype으로 확인 가능하다
print(img.dtype) # uint8


### 이미지의 ROI
# 이미지 작업시에는 특정 pixel단위보다 특정 영역 단위로 작업을 하게 된다
# 이것을 Region of Image(ROI)라고 한다. ROI설저은 Numpy의 Indexing 방법을 사용한다
# 만일 아래와 같은 특정 영역에 어떤 물체가 있다는 것을 알고있으면 그 영역을 설정해서 복사할 수도 있다
img2 = cv2.imread('baseball.jpg')
ball = img2[430:475, 817:884]
img2[491:536, 817:884] = ball # 아래쪽 행에 ball을 복사한다



### 이미지의 채널(Channel)
# 컬러 이미지는 3개의 채널 B, G, R로 구성되어 있습니다. 이를 채널별로 분리할 수 있습니다
# cv2.split() 함수는 비용이 많이 드는 함수입니다. 가능하다면 Numpy indexing 을 활용
b, g, r = cv2.split(img2)
img2 = cv2.merge((r, g, b))

# 또는 Numpy indexing 접근 방법으로 표현할 수 있습니다
b = img2[:, :, 0] # 0: B, 1: G, 2: R

# 특정 채널의 값을 변경하려면 아래와 같이 입력
img2[:,:,2] = 0 # Red Channel을 0으로 변경 => Red를 제거하는 효과


cv2.imshow('image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()