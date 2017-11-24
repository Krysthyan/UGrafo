from src.algoritmos.algoritmos import hilo_avara2
from src.grafo.Grafo import IAGraph

grafo = IAGraph('../../../static_files/test.csv')
# grafo = IAGraph(10000)
print("ddkkd")



hilo_avara2([grafo.graph['S']], grafo.graph['G'], [], [])