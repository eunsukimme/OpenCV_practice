# -*- coding: utf-8 -*- 
import cv2
from matplotlib import pyplot as plt

# 이미지 읽기
# imread(이미지 파일 경로, 읽는 옵션) - 이미지 파일을 읽고 numpy.ndarray 타입의 이미지 객체 행렬 리턴
img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)  # 이미지를 컬러로 읽어들인다(투명 무시)
grey = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)  # 이미지를 그레이 스케일로 읽음
unchanged = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED) # 이미지를 투명도 까지 포함해서 읽음
print(img.shape)

# 이미지 보기
# imshow(윈도우 창 제목, imread리턴값(numpy.ndarray)) - 이미지를 사이즈에 맞게 보여준다
cv2.imshow('image', img)
cv2.imshow('grey', grey)
cv2.imshow('unchanged', unchanged)
cv2.waitKey(0)      # 키 입력을 대기. 0이면 무한 대기하며 아니면 밀리 초 후 종료한다
cv2.destroyAllWindows()  # 화면에 나타난 윈도우 종료. 일반적으로 이 세개 같이 사용된다

# 이미지 보기(matplotlib)
# Matplotlib는 다양한 plot 기능을 가진 Python Plot Library이다
# 이미지를 줌 하거나 화면에 여러개의 이미지를 보고자 할 때 유용하다
plt.imshow(img)
plt.xticks([])  # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()

# 이 떄 파란색 계열의 사진이 나타난다. 이유는 openCV는 BGR을 사용하지만, Matplotlib는 RGB를 사용한다
# 3차원 배열(R, G, B) 중 첫 번째와 세 번째 값을 바꿔주면 된다
b, g, r = cv2.split(img)  # 이미지를 b, g, r 로 분리
img2 = cv2.merge([r, g, b])  # b, r을 바꿔서 merge 한다

plt.imshow(img2)
plt.xticks([])  # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()


# 이미지 저장
# imwrite(저장할 파일명, 저장할 이미지) - 이미지나 동영상의 특정 프레임을 저장한다
cv2.imwrite('lenagray.png', grey)

