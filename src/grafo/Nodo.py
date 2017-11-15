class Node:
    def __init__(self, name, weight=None):
        self.name = name
        self.weight = weight
        
        self.result = []
        self.sons = []
        self.roots = []

    def add_node(self, node, weight):
        node.roots.append((self, weight))
        self.sons.append((node, weight))
        
        self.sons.sort(key=lambda x: x[0].name)

    def get_path(self):
        [(print(node[0].name), node[0].get_path()) for node in self.sons]

    def get_level(self):
        if not self.sons:
            return 1
        while self.sons:
            return self.sons[0][0].get_level() + 1

    def search_node(self, name, path=[]):
        for node in self.sons:
            if node[0].name is name:
                path.append(node)
                break
            node[0].search_node(name)

    def get_root(self):
        print(self.roots)

    def get_roots(self):
        if self.roots:
            self.result = [(print(node[0].name), node[0].get_roots()) for node in self.roots]
