import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QVBoxLayout,QWidget

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(300,300)
        self.setWindowTitle("Malone")
        layout =QVBoxLayout()

        btn1 = QPushButton("按钮1")
        layout.addWidget(btn1)
        layout.addStretch(1)
        btn2 = QPushButton("按钮2")
        layout.addWidget(btn2)
        layout.addStretch(2)
        btn3 = QPushButton("按钮3")
        layout.addWidget(btn3)
        layout.addStretch(2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)        
    win = MyWindow()
    win.show()
    app.exec_()