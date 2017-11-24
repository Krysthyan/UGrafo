import sys
import threading
from multiprocessing.pool import ThreadPool
from queue import Queue

from PyQt5 import uic
from PyQt5.QtWidgets import QCheckBox, QHeaderView, QComboBox, QMainWindow, QApplication, QTableWidgetItem

from src.grafo.Grafo import IAGraph

form_class = uic.loadUiType("./src/ui/disenos/Ugrafo.ui")[0]


class Win_algoritmos(QMainWindow, form_class):
    def __init__(self, grafo, parent):
        self.grafo = grafo
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.ver_grafo.clicked.connect(self.ver_grafo_clicked)
        self.btn_atras.clicked.connect(self.regresar_win_init)
        self.btn_buscar.clicked.connect(self.buscar_algoritmos)
        self.cargar_nodos_init_end()
        self.tabla_algoritmos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def ver_grafo_clicked(self):
        self.grafo.draw()

    def cargar_nodos_init_end(self):
        for nodo in self.grafo.graph:
            self.comboBox_init.addItem(str(nodo))
            self.comboBox_end.addItem(str(nodo))

    def regresar_win_init(self):
        self.destroy()
        self.parent().show()


    def buscar_algoritmos(self):
        nodo_inicial = self.grafo.graph[self.comboBox_init.currentText()]
        nodo_final = self.grafo.graph[self.comboBox_end.currentText()]

        t1 = threading.Thread(self.busqueda_anchura(nodo_inicial, nodo_final))
        t2 = threading.Thread(self.busqueda_profundidad(nodo_inicial, nodo_final))
        t3 = threading.Thread(self.busqueda_coste_uniforme(nodo_inicial, nodo_final))
        t4 = threading.Thread(self.busqueda_ascenso_camino(nodo_inicial, nodo_final))
        t5 = threading.Thread(self.busqueda_primero_el_mejor(nodo_inicial, nodo_final))
        t6 = threading.Thread(self.busqueda_a_estrella(nodo_inicial, nodo_final))
        t7 = threading.Thread(self.busqueda_bidireccional(nodo_inicial, nodo_final))
        t8 = threading.Thread(self.busqueda_avara(nodo_inicial, nodo_final))
        t9 = threading.Thread(self.busqueda_iterativa(nodo_inicial, nodo_final))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()

    def busqueda_anchura(self, nodo_inicial, nodo_final):
        time, list_return_nodes = self.grafo.busqueda_anchura(nodo_inicial, [nodo_final])
        self.create_combo_box(time, list_return_nodes, 0, 1, 0, 0)

    def busqueda_profundidad(self, nodo_inicial, nodo_final):
        time, list_result_nodes = self.grafo.busqueda_profundidad(nodo_inicial, [nodo_final])


        self.create_combo_box(time, list_result_nodes, 1, 1, 1, 0)

    def busqueda_bidireccional(self, nodo_inicial, nodo_final):
        time, list_result_nodes = self.grafo.busqueda_bidireccional(nodo_inicial, nodo_final)
        self.create_combo_box(time, list_result_nodes, 2, 1, 2, 0)

    def busqueda_avara(self, nodo_inicial, nodo_final):
        time, list_result_nodes = self.grafo.avara(nodo_inicial, nodo_final)
        self.create_combo_box(time, list_result_nodes, 8, 1, 8, 0)


    def busqueda_iterativa(self, nodo_inicial, nodo_final):
        comboBoxAnchura1 = QComboBox()
        tiempo_DFS, busqueda_profundidad = self.grafo.busqueda_iterativa(
            self.grafo.graph[self.comboBox_init.currentText()],
            self.grafo.graph[self.comboBox_end.currentText()])

        if busqueda_profundidad is not None:
            for bus in busqueda_profundidad:
                comboBoxAnchura1.addItem(' '.join(str(x[0].name) for x in bus))
        else:
            comboBoxAnchura1.addItem('No hay camino')
        self.tabla_algoritmos.setCellWidget(3, 1, comboBoxAnchura1)
        self.tabla_algoritmos.setItem(3, 0, QTableWidgetItem(str('%.10f' % tiempo_DFS)))

    def busqueda_coste_uniforme(self, nodo_inicial, nodo_final):
        comboBoxAnchura1 = QComboBox()
        CUS, busqueda_profundidad = self.grafo.costo_uniforme(
            self.grafo.graph[self.comboBox_init.currentText()],
            self.grafo.graph[self.comboBox_end.currentText()])
        if busqueda_profundidad[1] is not None:
            comboBoxAnchura1.addItem('Costo : ' + str(busqueda_profundidad[1]))
            for bus in busqueda_profundidad[0]:
                comboBoxAnchura1.addItem(str(bus.name))
        else:
            comboBoxAnchura1.addItem('No hay camino')

        self.tabla_algoritmos.setCellWidget(4, 1, comboBoxAnchura1)
        self.tabla_algoritmos.setItem(4, 0, QTableWidgetItem(str('%.10f' % CUS)))

    def busqueda_ascenso_camino(self, nodo_inicial, nodo_final):
        time, list_result_nodes = self.grafo.ascceso_camino(nodo_inicial, nodo_final)
        self.create_combo_box(time, list_result_nodes, 5, 1, 5, 0)

    def busqueda_primero_el_mejor(self, nodo_inicial, nodo_final):
        time, list_result_nodes = self.grafo.primero_el_mejor(nodo_inicial, nodo_final)
        self.create_combo_box(time, list_result_nodes, 6, 1, 6, 0)


    def busqueda_a_estrella(self, nodo_inicial, nodo_final):
        comboBoxAnchura1 = QComboBox()
        CUS, busqueda_profundidad = self.grafo.a_estrella(
            self.grafo.graph[self.comboBox_init.currentText()],
            self.grafo.graph[self.comboBox_end.currentText()])

        if busqueda_profundidad[0] is not None:
            comboBoxAnchura1.addItem('Costo : ' + str(busqueda_profundidad[1]))
            for bus in busqueda_profundidad[0]:
                comboBoxAnchura1.addItem(str(bus.name))
        else:
            comboBoxAnchura1.addItem('No hay camino')
        self.tabla_algoritmos.setCellWidget(7, 1, comboBoxAnchura1)
        self.tabla_algoritmos.setItem(7, 0, QTableWidgetItem(str('%.10f' % CUS)))

    def create_combo_box(self, time, list_result_nodes, x_node, y_node, x_time, y_time):
        combo_box_result_nodes = QComboBox()
        if list_result_nodes is not None:
            for bus in list_result_nodes:
                combo_box_result_nodes.addItem(str(bus.name))
        else:
            combo_box_result_nodes.addItem('No hay camino')
        self.tabla_algoritmos.setCellWidget(x_node, y_node, combo_box_result_nodes)
        self.tabla_algoritmos.setItem(x_time, y_time, QTableWidgetItem(str('%.10f' % time)))
