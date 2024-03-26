import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Malone")
    button = QPushButton("退出",win)
    button.clicked.connect(win.close)
    # button.setParent(win)
    win.show()
    app.exec_()