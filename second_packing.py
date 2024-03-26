from PySide2.QtWidgets  import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox

class states:
    def __init__(self):
        self.window=QMainWindow()
        self.window.setWindowTitle("Salary Statistics")
        self.window.resize(630,400)
        self.window.move(300,310)

        self.textEdit=QPlainTextEdit(self.window)
        self.textEdit.resize(300,350)
        self.textEdit.setPlaceholderText("Please input salary table")
        self.textEdit.move(10,15)

        self.button=QPushButton("To Compile Statistics",self.window)
        self.button.resize(300,50)
        self.button.move(320,80)
        self.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info=self.textEdit.toPlainText()

        salary_20k_above=''
        salary_20k_below=''

        for line in info.splitlines():
            if not line.strip():
                continue
            parts=line.split(" ")
            parts=[p for p in parts if p]
            name,salary,age=parts

            if int(salary)>20000:
                salary_20k_above+=name+'\n'
            else:
                salary_20k_below+=name+'\n'
        
        QMessageBox.about(self.window,"Statical Results",f"Employees with salaries above 20k are\n{salary_20k_above}\
                          \nEmployees with salaries below 20k are\n{salary_20k_below}")



app=QApplication([])
state=states()
state.window.show()
app.exec_()
