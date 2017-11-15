from random import randint

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
