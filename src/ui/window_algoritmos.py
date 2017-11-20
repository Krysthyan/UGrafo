from PyQt5 import uic
from PyQt5.QtWidgets import QCheckBox, QHeaderView, QComboBox, QMainWindow

from src.grafo.Grafo import IAGraph

form_class = uic.loadUiType("./src/ui/disenos/Ugrafo.ui")[0]


class Win_algoritmos(QMainWindow, form_class):
    def __init__(self, path, parent=None):
        self.path = path
        self.grafo = IAGraph(self.path)
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.nodos_inicio = QComboBox()

        self.nodos_inicio.addItem('Nodo 1')
        self.ver_grafo.clicked.connect(self.ver_grafo_clicked)
        self.cargar_nodos_init_end()



        self.tabla_algoritmos.setCellWidget(0, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(1, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(2, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(3, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(4, 2, QCheckBox())
        self.tabla_algoritmos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def ver_grafo_clicked(self):

        self.grafo.draw()

    def cargar_nodos_init_end(self):
        for nodo in self.grafo.graph:
            self.comboBox_init.addItem(nodo)
            self.comboBox_end.addItem(nodo)