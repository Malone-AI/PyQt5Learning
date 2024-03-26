from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class Stats:
    def __init__(self):
        qfile_stats=QFile("PyQt5_Learning/UI/Salary_statistic.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui=QUiLoader().load(qfile_stats)

        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
            info=self.ui.textEdit.toPlainText()

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

            QMessageBox.about(self.ui,"Statical Results",f"Employees with salaries above 20k are\n{salary_20k_above}\
                              \nEmployees with salaries below 20k are\n{salary_20k_below}")

app=QApplication([])
stats=Stats()
stats.ui.show()
app.exec_()