import timeit
from random import randint
import time

from src.algoritmos.algoritmos import BFS, DFS, CUS, bsuqueda_ascenso_colina, busqueda_primero_el_mejor, \
    busqueda_a_estrella, BS, BPI, busqueda_avara
from src.algoritmos.recursos import read_graph, random_graph, draw_graph



class IAGraph:
    def __init__(self, path=None):
        if type(path) is int or path is None:
            if path is None:
                path = randint(10, 20)
            self.graph = random_graph(path)
        if type(path) is str:
            self.graph = read_graph(path)

    def draw(self):
        draw_graph(self.graph)

    def busqueda_anchura(self, node_root, nodes_end):
        tiempo_inicial = time.process_time()
        result = BFS(node_root, nodes_end)
        return time.process_time() - tiempo_inicial, result

    def busqueda_profundidad(self, node_root, nodes_end):
        tiempo_inicial = time.process_time()
        result = DFS(node_root, nodes_end)
        return time.process_time() - tiempo_inicial, result

    def busqueda_bidireccional(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        hilo = BS(node_root, node_end)
        return time.process_time() - tiempo_inicial, hilo

    def busqueda_iterativa(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        result = BPI(node_root, node_end)
        return time.process_time() - tiempo_inicial, result

    def costo_uniforme(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        result = CUS(node_root, node_end)
        return time.process_time() - tiempo_inicial, result

    def ascceso_camino(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        result = bsuqueda_ascenso_colina(node_root, node_end)
        return time.process_time() - tiempo_inicial, result

    def primero_el_mejor(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        result = busqueda_primero_el_mejor(node_root, [node_end])
        return time.process_time() - tiempo_inicial, result

    def a_estrella(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        result = busqueda_a_estrella(node_root, node_end)
        return time.process_time() - tiempo_inicial, result

    def avara(self, node_root, node_end):
        tiempo_inicial = time.process_time()
        hilo = busqueda_avara(node_root, node_end)
        return time.process_time() - tiempo_inicial, hilo