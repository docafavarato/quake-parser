import sys
import pyperclip
from quakeParser import quakeParser
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import *

class Ui(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent=parent)
        uic.loadUi("main.ui", self)
        self.show()
        
        self.setFixedSize(self.size())
        self.pickFile.clicked.connect(self.parse_file)
        self.copy.clicked.connect(self.copy_result)
        
    def parse_file(self):
        file = str(QFileDialog.getOpenFileName(self, "Selecione o arquivo")).split(",")[0].split("(")[1].replace("'", "")
        quakeParser(file)
        
        with open("output/data.json", "r") as output:
            data = output.read()
            self.result.setText(data)
        
    def copy_result(self):
        pyperclip.copy(self.result.toPlainText())
        QMessageBox.information(self, "Sucesso", "O resultado foi copiado para a área de transferência.")
        
app = QApplication(sys.argv)
window = Ui()
app.exec_()