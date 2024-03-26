import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QLabel,QDesktopWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("QQ")
    win.resize(380,130)

    label = QLabel("账号",win)
    label.setGeometry(20,20,30,30)
    label_pwd =QLabel("密码",win)
    label_pwd.setGeometry(20,50,30,30)

    edit = QLineEdit(win)
    edit.setPlaceholderText("请输入您的账号")
    edit.setGeometry(60,20,300,30)
    edit2 = QLineEdit(win)
    edit2.setPlaceholderText("请输入您的密码")
    edit2.setGeometry(60,50,300,30)

    button_log = QPushButton("登录",win)
    button_log.setGeometry(150,90,80,30)

    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    old_x,old_y,width,height = win.frameGeometry().getRect()

    win.move(x - width / 2,y - height / 2)
    win.show()
    app.exec_()