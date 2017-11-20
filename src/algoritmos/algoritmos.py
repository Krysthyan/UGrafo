from src.grafo.Nodo import Node


# busqueda por anchura.
def BFS(node_root, nodes_end: object):
    cola = [node_root]
    output = []
    while cola and nodes_end:
        evalue_node = cola[0]
        for node_son, _ in evalue_node.sons:
            if not node_son in cola and not node_son in output:
                cola.append(node_son)
        if evalue_node in nodes_end:
            nodes_end.remove(evalue_node)
        output.append(evalue_node)
        del cola[0]
    return output


# busqueda en profundidad.
def DFS(node_root, nodes_end: list):
    cola = [node_root]
    output = []
    while cola and nodes_end:
        evalue_node = cola[0]
        for node_son, _ in evalue_node.sons.__reversed__():
            if not node_son in cola and not node_son in output:
                cola = [node_son] + cola
        if evalue_node in nodes_end:
            nodes_end.remove(evalue_node)
        output.append(evalue_node)
        cola.remove(evalue_node)
    return output


def func1(node_root, nodes_end: list, level):
    level_tem = level
    cola = [(node_root, level_tem - level)]
    output = []
    while cola and nodes_end:
        evalue_node = cola[0]
        if evalue_node[1] <= level_tem or level > 0:
            level -= 1
            for node_son, _ in evalue_node[0].sons.__reversed__():
                bandera = True

                for test in cola:
                    if test[0] is node_son:
                        bandera = False
                for test in output:
                    if test[0] is node_son:
                        bandera = False
                if bandera:
                    cola = [(node_son, level_tem - level)] + cola

        if evalue_node in nodes_end:
            nodes_end.remove(evalue_node)
        output.append(evalue_node)
        cola.remove(evalue_node)
    return output


def func(node_root, nodes_end: object):
    salida = [[(node_root, 0)]]
    level = 0
    tag = True
    while tag:
        salida.append(func1(node_root, [nodes_end], level))
        level += 1
        for sal in salida:
            for sal1 in sal:
                if sal1[0] is nodes_end:
                    tag = False

    return salida


# busqueda por profundidad iterativa.
def BPI(node_root, nodes_end: object):
    return func(node_root, nodes_end)


# busqueda bidireccional.
def BS():
    pass


# busqueda de costo uniformes.
def CUS(node_root, nodes_end):
    pass
