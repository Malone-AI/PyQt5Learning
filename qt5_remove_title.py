"""
    去除标题栏
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5 import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowFlags(Qt.Qt.CustomizeWindowHint)
    win.resize(300,300)
    button = QPushButton("X",win)
    button.setGeometry(270,0,30,30)
    button.clicked.connect(win.close)
    win.show()
    app.exec_()