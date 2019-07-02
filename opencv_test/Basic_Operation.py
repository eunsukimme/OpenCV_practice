import cv2
import numpy as np

img = cv2.imread('lena.jpg')
print(img.shape, img.size, img.dtype)


px = img[100, 200]
print(px) # BGR순

print(img.item(100, 200, 1))
img.itemset((100, 200, 1), 255)
print(img.item(100, 200, 1))


img = cv2.imread('baseball-player.jpg')
ball = img[440:485, 817:884] # img[행의 시작점:행의 끝점, 열의 시작점:열의 끝점]
img[500:545, 817:884] = ball

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 Channels
b, g, r = cv2.split(img)
img = cv2.merge((r, g, b))

b = img[:, :, 0]

img[:, :, 2] = 0 # Red Channel을 0으로 변경. Red 제거하는 효과