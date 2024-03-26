"""
    抽屉布局QStackedLayout
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QStackedLayout,QLabel

class win(QWidget):
    def __init__(self,num,color):
        super(win,self).__init__()
        QLabel(f"我是抽屉{num}要显示的内容",self)
        self.setStyleSheet("background-color:" + color + ";")


class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.create_stacked_layout()
        self.init_ui()
    
    def create_stacked_layout(self):
        self.stacked_layout = QStackedLayout()
        win1 = win(1,"red")
        win2 = win(2,"green")
        win3 = win(3,"blue")
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)
        self.stacked_layout.addWidget(win3)

    def init_ui(self):
        self.setFixedSize(300,270)

        container = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:gray;")
        btn1 = QPushButton("抽屉1")
        btn2 = QPushButton("抽屉2")
        btn3 = QPushButton("抽屉3")

        btn1.clicked.connect(self.btn_press1)
        btn2.clicked.connect(self.btn_press2)
        btn3.clicked.connect(self.btn_press3)

        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)
        container.addWidget(btn3)

        self.setLayout(container)
    
    def btn_press1(self):
        self.stacked_layout.setCurrentIndex(0)
    def btn_press2(self):
        self.stacked_layout.setCurrentIndex(1)
    def btn_press3(self):
        self.stacked_layout.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()