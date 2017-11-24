import sys
from PyQt5.QtWidgets import QApplication
from src.ui.Ugrafo import Ugrafo

app = QApplication(sys.argv)
MyWindow = Ugrafo(None)

MyWindow.show()
app.exec_()