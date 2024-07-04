import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from AltinoLite import *

import time

form_class = uic.loadUiType("altino.ui")[0]

connectFlag = False

#쓰레드 선언
class Thread1(QThread):
    updateSignal = pyqtSignal(int)
    def run(self):
        while (connectFlag == True) :
            #센서 값을 시그널로 보냅니다
            time.sleep(0.05)
            self.updateSignal.emit("test")

class MyWindow(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 내가 원하는 기능들을 추가
        self.btnConnectAltino.clicked.connect(self.fn_ConnectAltino)
        self.btnDisConnectAltino.clicked.connect(self.fn_btnDisConnectAltino)
        self.btnGo.clicked.connect(self.fn_Go)
        self.btnstop.clicked.connect(self.fn_stop)
        self.btnback.clicked.connect(self.fn_back)
        self.btnLeft.clicked.connect(self.fn_Left)
        self.btnRight.clicked.connect(self.fn_Right)
        #self.btnSentor.clicked.connect(self.fn_Senter)
    
        self.thread = Thread1()
        self.thread.updateSignal.connect(self.updateSensor)

    # 알티노를 연결한다
    def fn_ConnectAltino(self) :
        Open()
        self.txtAltinoStatus.setText("연결완료")
        global connectFlag
        connectFlag = True
        self.thread.start()

    def updateSensor(self, value) :
        # print("왔다!!")
        self.txtCDS.setText(str(sensor.CDS))

    # 알티노 연결 해제
    def fn_btnDisConnectAltino(self) :
        Close()
        connectFlag = False
        self.txtAltinoStatus.setText("미 연결")
    # Go
    def fn_Go(self) :
        Go(300,300)
    # stop
    def fn_stop(self) :
        Go(0,0)
    # back
    def fn_back(self) :
        Go(-300,-300)
    # Left
    def fn_Left(self) :
        Steering(-127)
    # Right
    def fn_Right(self) :
        Steering(127)
    #def fn_Senter(self) :
    #    Steering(0)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()