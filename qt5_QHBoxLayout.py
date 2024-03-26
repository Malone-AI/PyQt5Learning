import sys
from PyQt5.QtWidgets import QApplication,QWidget,QRadioButton,QGroupBox,QVBoxLayout,QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()
        self.init_ui()
    
    def init_ui(self):
        self.resize(120,120)

        container = QVBoxLayout()

        hobby_box = QGroupBox("爱好")
        hobby_vbox = QVBoxLayout()

        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("烫头")

        hobby_vbox.addWidget(btn1)
        hobby_vbox.addWidget(btn2)
        hobby_vbox.addWidget(btn3)
        hobby_box.setLayout(hobby_vbox)


        sex_box = QGroupBox("性别")
        sex_hbox = QHBoxLayout()

        b1 = QRadioButton("男")
        b2 = QRadioButton("女")

        sex_hbox.addWidget(b1)
        sex_hbox.addWidget(b2)
        sex_box.setLayout(sex_hbox)

        container.addWidget(hobby_box)
        container.addWidget(sex_box)

        self.setLayout(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()