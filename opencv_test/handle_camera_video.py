import cv2

# cap 이 정상적으로 open 되었는 지 확인하기 위해서 cap.isOpen()으로 확인가능
cap = cv2.VideoCapture()

# cap.get(prodId)/cap.set(propId, value)을 통해서 속성 변경이 가능
# 3은 width, 4는 height

print("width: {0}, height: {1}".format(cap.get(3), cap.get(4)))
cap.set(3, 320)
cap.set(4, 240)

while cap.isOpened():
    # ret : frame capture 결과 (boolean)
    # frame : Capture한 frame
    ret, frame = cap.read()

    if ret:
        # image를 Grayscale로 Convert함.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('img', frame)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
