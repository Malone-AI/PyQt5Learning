"""
    信号与槽
"""
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Win(QWidget):
    # 自定义信号
    my_signal = pyqtSignal(str)
    def __init__(self):
        super(Win,self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500,300)
        btn = QPushButton("Click me",self)
        btn.clicked.connect(self.btn_click)

        # 绑定信号与槽
        self.my_signal.connect(self.my_signal_react)
    
    def btn_click(self):
        ip_set = [f"192.168.1.{i}" for i in range(0,256)]
        for i , ip in enumerate(ip_set):
            print(f"模拟，正在检查",ip,end = "")
            if i % 5 == 0:
                self.my_signal.emit("【发现漏洞】")
            else:
                self.my_signal.emit("")
            time.sleep(0.01)
    
    def my_signal_react(self,p):
        print(p)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    app.exec_()