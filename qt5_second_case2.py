import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5 import uic

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.init_ui()
    
    def init_ui(self):
        self.ui = uic.loadUi("PyQt5_Learning/UI/QQ.ui")
        self.username = self.ui.lineEdit
        self.password = self.ui.lineEdit_2
        self.login_btn = self.ui.pushButton
        self.login_btn.clicked.connect(self.login)
        self.text_browser = self.ui.textBrowser

    def login(self):
        if self.username.text() == "":
            self.text_browser.setText("请输入用户名！")
        elif self.username.text() == "admin":
            if self.password.text() == "123456":
                self.text_browser.setText(f"欢迎{self.username.text()}")
            elif self.password.text() == "":
                self.text_browser.setText("请输入密码！")
            else:
                self.text_browser.setText("密码错误！")
        else:
            self.text_browser.setText("用户不存在！")
        self.text_browser.repaint()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.ui.show()
    app.exec_()