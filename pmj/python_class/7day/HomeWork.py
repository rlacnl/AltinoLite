import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("altino.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 내가 원하는 기능들을 추가
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()