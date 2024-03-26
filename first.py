from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit

app=QApplication([])

win=QMainWindow()
win.resize(500,400)
win.move(300,310)
win.setWindowTitle("薪资统计")

textEdit=QPlainTextEdit(win)
textEdit.resize(300,350)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)

button=QPushButton("统计",win)
button.move(380,80)

win.show()

app.exec_()