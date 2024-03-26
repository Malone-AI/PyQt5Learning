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

    def login(self):
        print("正在登陆中......")
        if self.username.text() == "admin":
            if self.password.text() == "123456":
                print("登录成功")
                self.close()
            else:
                QMessageBox.about(self.ui,"提示","密码错误!")
        else:
            QMessageBox.about(self.ui,"提示","用户不存在!")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.ui.show()
    app.exec_()