from ..grafo import Nodo as node
import csv
from random import randint
import networkx as nx
import matplotlib.pyplot as plt


def __add_node_read(key, values, dic_graph):
    if str(values[0]) not in dic_graph:
        dic_graph[str(values[0])] = node.Node(str(values[0]), values[2])
    dic_graph[str(key)].add_node(dic_graph[str(values[0])], values[3])


def random_graph(size, dic_graph={}):
    for a in range(size + 1):
        if str(a) not in dic_graph:
            dic_graph[str(a)] = node.Node(str(a), randint(1, size))
        for _ in range(randint(1, 3)):
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
            edges_from.append((key +'-'+ str(value.weight), node_son[0].name+'-'+str(node_son[0].weight), node_son[1]))
    return edges_from


def draw_graph(dic_graph):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(__get_edges_from(dic_graph), with_labels=True)

    elarge = [(u, v) for (u, v, d) in graph.edges(data=True) if float(d['weight']) > 0.5]
    esmall = [(u, v) for (u, v, d) in graph.edges(data=True) if float(d['weight']) <= 0.5]

    pos = nx.spring_layout(graph)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='orange')

    # edges
    nx.draw_networkx_edges(graph, pos, edgelist=elarge, width=1, edge_color='g')
    nx.draw_networkx_edges(graph, pos, edgelist=esmall, arrows=True, width=10000,
                           alpha=1.5, edge_color='b', style='solid')

    # labels
    nx.draw_networkx_labels(graph, pos, font_size=8, font_family='sans-serif')

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.axis('off')
    plt.draw()
    plt.show()
