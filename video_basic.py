# -*- coding: utf-8 -*-

# Camera로부터 영상을 읽어, 화면에 보여주기 위해서 아래와 같은 순서로 진행한다

# 1. VedioCapture 오브젝트를 생성한다. 변수로 camera device index나 동영상 파일명을 넘겨준다.
#    일반적으로 0 이면 Camera와 연결된다
# 2. Loop를 돌면서 frame을 읽어들인다
# 3. 읽은 frame에 대해서 변환 작업을 수행한 후, 화면에 보여준다
# 4. 영상 재생이 끝나면, VideoCapture 오브젝트를 release하고 창을 닫는다

import cv2

# cap이 정상적으로 open이 되었는지 확인하기 위해 cap.isOpen() 으로 확인가능

cap = cv2.VideoCapture(0)


# cap.get(prodId)/cap.set(propId, value)를 통해서 속성 변경이 가능하다
# 3은 width, 4는 height

print('width: {0}, heigth: {1}'.format(cap.get(3), cap.get(4)))
cap.set(3, 320)
cap.set(4, 240)


# 파일로부터 동영상 재생도 Camera 에서의 영상 재생과 동일하다
#cap = cv2.VideoCapture('vtest.mp4')

# 영상 저장
# 영상을 저장하기 위해선 cv2.VideoWriter 오브젝트를 생성해야 한다
# VideoWriter(저장될 파일명, 코덱 정보, 초당 저장할 frame, 저장할 사이즈)
'''
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (640, 480))
'''

# 동영상 촬영
'''
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        # 이미지 반전, 0: 상하, 1: 좌우
        frame = cv2.flip(frame, 0)

        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break
'''

# 동영상 촬영
while(cap.isOpened()):
    # ret: frame capture 결과(boolean)
    # frame: Capture한 frame
    ret, frame = cap.read()

    if(ret):
        # image를 그레이 스케일로 변화한다
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', grey)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break


cap.release()
#out.release()
cv2.destroyAllWindows()
