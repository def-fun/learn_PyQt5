from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtCore import QFile
from PyQt5 import uic


class State():
    def __init__(self):
        # qfile_stats = QFile('untitled.ui')
        # qfile_stats.open(QFile.ReadOnly)
        # qfile_stats.close()

        self.ui = uic.loadUi('untitled.ui')
        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()
        print(info)


app = QApplication([])
stats = State()
stats.ui.show()
app.exec_()
