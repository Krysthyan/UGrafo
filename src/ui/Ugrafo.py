from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from src.ui.window_algoritmos import Win_algoritmos

form_class = uic.loadUiType("./src/ui/disenos/main.ui")[0]


class Ugrafo(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.abrir_grafo.clicked.connect(self.arbir_grafo_btn)
        self.crear_grafo_aleatorio.clicked.connect(self.crear_grafo_aleatorio_btn)

    def arbir_grafo_btn(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.close()
            ventana_nueva = Win_algoritmos(fileName, self)
            ventana_nueva.show()

    def crear_grafo_aleatorio_btn(self):
        if len(self.line_num_aleatorio.text()):
            ventana_nueva = Win_algoritmos(int(self.line_num_aleatorio.text()), self)

        else:
            ventana_nueva = Win_algoritmos(None, self)
        self.close()
        ventana_nueva.show()
