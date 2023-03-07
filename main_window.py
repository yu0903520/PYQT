import sys,time
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from test8 import Ui_Form

ocv = True   
fourcc = cv2.VideoWriter_fourcc(*'mp4v')   # 設定存檔影片格式
recorderType = False                        # 設定是否處於錄影狀態，預設 False
output = None
depth=6   # 深度數值
frequency=30   # 頻率
round=1   # 回合數
left=100   #左手角度
right=0   #右手角度

# 存檔時使用時間名稱的函式
def rename():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return str(timestr).replace('.','')
                              
# 設定 output 初始值為 None

class Camera(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 設置攝像頭
        self.cap = cv2.VideoCapture(0)

        # 設置計時器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)
        self.startVideo.clicked.connect(self.start_video)
        self.stopVideo.clicked.connect(self.stop_video)
        self.exit_btn.clicked.connect(self.exit)
        
        # 初始化 self.frame 變數
        self.frame = None


    def get_angle_point(human, pos):
        # 返回各个部位的关键点
        pnts = []

        if pos == 'left_elbow':
            pos_list = (5, 6, 7)
        elif pos == 'left_hand':
            pos_list = (1, 5, 7)
        elif pos == 'left_knee':
            pos_list = (12, 13, 14)
        elif pos == 'left_ankle':
            pos_list = (5, 12, 14)
        elif pos == 'right_elbow':
            pos_list = (2, 3, 4)
        elif pos == 'right_hand':
            pos_list = (1, 2, 4)
        elif pos == 'right_knee':
            pos_list = (9, 10, 11)
        elif pos == 'right_ankle':
            pos_list = (2, 9, 11)
        else:
            print('Unknown  [%s]', pos)
            return

        for i in range(3):
            if human[pos_list[i]][2] <= 0.1:
                print('component [%d] incomplete' % (pos_list[i]))
                return pnts
            pnts.append((int(human[pos_list[i]][0]), int(human[pos_list[i]][1])))
        return pnts
    

    def angle_between_points(p0, p1, p2):
        # 计算角度
        a = (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
        b = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        c = (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2
        try:
            if a * b == 0:
                return -1.0
            else:
                angle = math.acos((a + b - c) / math.sqrt(4 * a * b)) * 180 / math.pi
        except:
            angle == -1
        return angle
    

    def angle_left_elbow(human):
        pnts = get_angle_point(human, 'left_elbow')
        if len(pnts) != 3:
            print('component incomplete')
            return

        angle = 0
        if pnts is not None:
            angle = angle_between_points(pnts[0], pnts[1], pnts[2])
            # print('left elbow angle:%f' % (angle))
        return angle


    def angle_right_elbow(human):
        pnts = get_angle_point(human, 'right_elbow')
        if len(pnts) != 3:
            print('component incomplete')
            return

        angle = 0
        if pnts is not None:
            angle = angle_between_points(pnts[0], pnts[1], pnts[2])
            # print('right elbow angle:%f' % (angle))
        return angle
    

    def update_frame(self):
        global recorderType, output, depth, frequency, round
        
        # 讀取攝像頭畫面
        ret, frame = self.cap.read()
        
        if ret:
            # 設定 self.frame 變數的值
            self.frame = frame
            # 按下錄影時，將檔案儲存到 output
            if recorderType == True and output is not None:
                output.write(self.frame)             
            
            # 將攝像頭畫面顯示在畫面上
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channels = image.shape
            bytes_per_line = channels * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.img_label.setPixmap(pixmap)

            # 顯示數值

            self.left.setText(str(left))
            self.right.setText(str(right))
            self.depthLabel.setText(str(depth))
            self.frequencyLabel.setText(str(frequency))
            self.round.setText(str(round))


    def start_video(self):
        global recorderType, output, height, width
        
        # 按下錄影時，將檔案儲存到 output
        if recorderType == True and output is not None:
            output.write(self.frame)             
        
        # 開始錄影
        if recorderType == False:
            # 取得當前攝像頭畫面的高度和寬度
            ret, frame = self.cap.read()
            if ret:
                height, width, channels = frame.shape
            
            # 設定錄影的檔案
            output = cv2.VideoWriter(rename() + ".mp4", fourcc, 20.0, (width, height))
                    
            recorderType = True

    def stop_video(self):
        global recorderType, output, depth
        # 釋放檔案資源
        if output is not None:
            output.release()                    # 釋放檔案資源
            recorderType = False                # 改為 False 表示停止錄影
    
    def exit(self):
        self.close()
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    camera = Camera()
    camera.show()
    sys.exit(app.exec_())