import cv2

cap = cv2.VideoCapture('final.mp4')

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 計數器
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_count += 1
        if frame_count % 6 == 0:
            cv2.imwrite(f"frame_{frame_count // 6}.jpg", frame) #存frame_coun%6==0
            # 引用副程式(frame)
            # 在這裡進行影像分析

        # 如果已經讀取了6幀，就退出迴圈
        if frame_count == 6:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



