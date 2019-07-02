import cv2
from matplotlib import pyplot as plt

# 이미지 경로, Option
# 1 cv2.IMREAD_COLOR : Color로 읽고, 투명한 부분은 무시한다. Default
# 0 cv2.IMREAD_GRAYSCALE Grayscale로 읽는다.
# -1 cv2.IMREAD_UNCHANGED : alphachannel까지 포함아여 읽는다.


"""
img1 = cv2.imread("lena.jpg", 1)
img2 = cv2.imread("lena.jpg", 0)

# title, cv2.imread()의 반환 값
cv2.imshow("image1", img1)
cv2.imshow("image2", img2)

k = cv2.waitKey()   # keyboard 입력을 대기하는 함수 (millisecond 단위, 0이면 무한대기)
if k == 27:
    cv2.destroyAllWindows() # 화면에 나타나 윈도우 종료
elif k == ord('s'):
    cv2.imwrite('lena_temp.jpg', img2)
    cv2.destroyAllWindows()
"""

img = cv2.imread('lena.jpg', 1)

b, g, r = cv2.split(img) # img 파일을 b,g,r로 분리
img1 = cv2.merge([r, g, b]) # b, r을 바꿔서 Merge

plt.imshow(img1)
plt.xticks([]) # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()

