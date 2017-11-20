# import sys
# from PyQt5.QtWidgets import QApplication
#
# from src.ui.Ugrafo import Ugrafo
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Ugrafo()
#     sys.exit(app.exec_())
# from src.grafo.Grafo import IAGraph
#
# grafo = IAGraph('./static_files/test.csv')
# for a in grafo.busqueda_anchura(grafo.graph['S'], [grafo.graph['C']]):
#     print(a.name)
# print('------------')
# for a in grafo.busqueda_profundidad(grafo.graph['S'], [grafo.graph['C']]):
#     print(a.name)
# print('hola mubndo')
# grafo.draw()

# !/usr/bin/python
# -*- coding: utf-8 -*-

# Convierte temperaturas
# www.pythondiario.com

import sys
from PyQt5 import uic

# Cargar nuestro archivo .ui
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QPushButton, QComboBox, QCheckBox

from src.grafo.Grafo import IAGraph

form_class = uic.loadUiType("./src/ui/disenos/Ugrafo.ui")[0]


class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.nodos_inicio = QComboBox()

        self.nodos_inicio.addItem('Nodo 1')
        self.ver_grafo.clicked.connect(self.ver_grafo_clicked)



        self.tabla_algoritmos.setCellWidget(0, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(1, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(2, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(3, 2, QCheckBox())
        self.tabla_algoritmos.setCellWidget(4, 2, QCheckBox())
        self.tabla_algoritmos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def ver_grafo_clicked(self):
        grafo = IAGraph('./static_files/test.csv')
        grafo.draw()



app = QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()