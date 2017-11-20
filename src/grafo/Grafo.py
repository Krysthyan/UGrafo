from random import randint

from src.algoritmos.algoritmos import BFS, DFS
from src.algoritmos.recursos import read_graph, random_graph, draw_graph
from src.grafo.Nodo import Node


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
        return BFS(node_root, nodes_end)

    def busqueda_profundidad(self, node_root, nodes_end):
        return DFS(node_root, nodes_end)
