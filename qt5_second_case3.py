import sys
import json
import time

from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5 import uic

class MyThread(QThread):
    start_login_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.start_login_signal.connect(self.login_by_request)
    
    def login_by_request(self,user_password_json):
        user_password_json = json.loads(user_password_json)
        print(user_password_json.get("user_name"))
        print(user_password_json.get("password"))
    
    def run(self):
        while True:
            print("子线程正在执行......")
            time.sleep(1)


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

        self.login_thread = MyThread()
        self.login_thread.start()

    def login(self):
        user_name =self.username.text()
        password = self.password.text()
        self.login_thread.start_login_signal.emit(json.dumps({"user_name":user_name,"password":password}))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.ui.show()
    app.exec_()