import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):
    my_signal = pyqtSignal(str)
    def __init__(self):
        super(MyWindow,self).__init__()
        self.label_history_text = list()
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon("PyQt5_Learning/R-C.png"))
        self.resize(500,200)
        container = QVBoxLayout()

        self.label = QLabel("")
        self.label.resize(440,15)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignTop)
        self.label.setStyleSheet("background-color: yellow;color: black;")

        scroll =QScrollArea()
        scroll.setWidget(self.label)
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(scroll)

        hbox_layout = QHBoxLayout()
        btn1 = QPushButton("开始检测",self)
        btn1.clicked.connect(self.check)
        self.my_signal.connect(self.signal_press)
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(btn1)
        hbox_layout.addStretch(1)

        container.addLayout(vbox_layout)
        container.addLayout(hbox_layout)
        self.setLayout(container)
    
    def check(self):
        for i,ip in enumerate([f"192.168.1.{x}" for x in range(1,256)]):
            self.my_signal.emit(ip + "【发现漏洞】")

    def signal_press(self,info):
        # print(info)
        self.label_history_text.append(info)
        self.label.setText("<br/>".join(self.label_history_text))
        self.label.resize(self.label.frameSize().width(),self.label.frameSize().height() + 15)
        self.label.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()