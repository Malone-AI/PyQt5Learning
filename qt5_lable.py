import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Malone")
    label = QLabel("Account",win)
    label.setGeometry(20,30,300,30)
    win.show()
    app.exec_()