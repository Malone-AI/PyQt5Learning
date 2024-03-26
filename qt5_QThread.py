import sys
import time
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QThread
from PyQt5 import uic

class My_Thread(QThread):
    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        for i in range(10):
            print("===多线程进程执行中===")
            time.sleep(0.5)

class My_Window(QWidget):
    def __init__(self):
        super(My_Window,self).__init__()
        self.init_ui()
    
    def init_ui(self):
        self.ui = uic.loadUi("PyQt5_Learning/UI/thread_1.ui")
        self.btn1 = self.ui.pushButton
        self.btn2 = self.ui.pushButton_2
        self.btn1.clicked.connect(self.btn1_work)
        self.btn2.clicked.connect(self.btn2_work)
    
    def btn1_work(self):
        for i in range(10):
            print("===UI线程执行中===")
            time.sleep(0.5)

    def btn2_work(self):
        self.Thread = My_Thread()
        self.Thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = My_Window()
    win.ui.show()
    app.exec()