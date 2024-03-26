import sys 
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("Malone")
    win.setWindowIcon(QIcon("PyQt5_Learning/R-C.png"))
    win.show()
    app.exec_()