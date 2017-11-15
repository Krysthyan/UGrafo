from ..grafo import Nodo as node
import csv
from random import randint
import networkx as nx
import matplotlib.pyplot as plt


def __add_node_read(key, values, dic_graph):

    if values[0] not in dic_graph:
        dic_graph[values[0]] = node.Node(values[0], values[2])
    dic_graph[key].add_node(dic_graph[values[0]], values[3])


def random_graph(size, dic_graph={}):
    for a in range(size + 1):
        if a not in dic_graph:
            dic_graph[a] = node.Node(a, randint(1, size))
        for b in range(randint(int(size / (size / 2)), int(size / (size / 3)))):
            __add_node_read(
                a,
                [randint(0, size), None, randint(1, size), randint(1, size)],
                dic_graph
            )
    return dic_graph


def read_graph(file_name, dic_graph={}):
    with open(file_name) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            if not row[0] in dic_graph:
                dic_graph[row[0]] = node.Node(row[0], row[2])
            __add_node_read(row[0], row[1:], dic_graph)

    return dic_graph


def __get_edges_from(dic_graph):
    edges_from = []
    for key, value in dic_graph.items():
        for node_son in value.sons:
            edges_from.append((key, node_son[0].name))
    return edges_from


def draw_graph(dic_graph):
    graph = nx.Graph()
    graph.add_edges_from(__get_edges_from(dic_graph))
    nx.draw_spring(graph, with_labels=True)
    plt.draw()
    plt.show()