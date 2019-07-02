import cv2
import numpy as np

drawing = False# Mouse 가 클릭된 상태인지 확인
mode = True # True 이면 사각형, Flase 이면 원
ix, iy = -1, -1


# callback 함수
def draw_circle(event, x, y, flags, param):
    global  ix,iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN: # 마우스를 누른 상태
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
        if drawing == True: # 마우스를 누른 상태 일 경우
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
            else:
               cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False # 마우스를 때면 상태 변경
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)

# 빈 Image 생성
#img = np.zeros((512, 512, 3), np.uint8)
img = np.full((512, 512, 3), 255, np.uint8)

print(img)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)

    k = cv2.waitKey(1)

    if k == ord('m'): # 사각형, 원 Mode 변경
        mode = not mode
    elif k == ord('q'): # esc를 누르면 종료
        break

cv2.destroyAllWindows()


