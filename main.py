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
from PyQt5.QtWidgets import QApplication

from src.ui.Ugrafo import Ugrafo

app = QApplication(sys.argv)
MyWindow = Ugrafo(None)

MyWindow.show()
app.exec_()