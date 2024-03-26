import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计算器")
        self.setWindowIcon(QIcon("PyQt5_Learning/R-C.png"))
        vbox = QVBoxLayout()
        gridbox = QGridLayout()

        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        vbox.addWidget(edit)

        data = {
            0:["7","8","9","+","("],
            1:["4","5","6","-",")"],
            2:["1","2","3","X","Backspace"],
            3:["0",".","=","/","C"]
        }
        for line_row,line_data in data.items():
            for line_col,content in enumerate(line_data):
                btn = QPushButton(content)
                gridbox.addWidget(btn,line_row,line_col)

        vbox.addLayout(gridbox)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()