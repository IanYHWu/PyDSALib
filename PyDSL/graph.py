
from PyDSL.queue import Queue
from PyDSL.stack import Stack


class Node:

    def __init__(self, key):
        self.key = key
        self.connections = {}
        self.colour = 'white'

    def add_nbr(self, nbr, weight):
        self.connections[nbr] = weight

    def get_nbrs(self):
        return self.connections.keys()

    def get_key(self):
        return self.key

    def get_weight(self, nbr):
        return self.connections[nbr]

    def set_colour(self, col):
        self.colour = col

    def get_colour(self):
        return self.colour

    def __repr__(self):
        return 'Node {}: contains connections to {}'.format(self.key, self.connections)


class Graph:

    def __init__(self):
        self.node_list = {}
        self.size = 0
        self.time = 0

    def add_node(self, key):
        self.size += 1
        new_node = Node(key)
        self.node_list[key] = new_node
        return new_node

    def get_node(self, key):
        if key in self.node_list:
            return self.node_list[key]
        else:
            return None

    def add_edge(self, key, edge, weight):
        target = self.get_node(key)
        if target:
            target.add_nbr(edge, weight)
        else:
            return 'Cannot add edge. Selected node does not exist'

    def add_undirected_edge(self, key, edge, weight):
        target = self.get_node(key)
        targeted = self.get_node(edge)
        if target and targeted:
            target.add_nbr(edge, weight)
            targeted.add_nbr(key, weight)
        else:
            return 'Cannot add undirected edge. One of the selected nodes does not exist'

    def get_vertices(self):
        return self.node_list.keys()
    
    def _bfs_visit(self, current_node):
        q = Queue()
        g = Graph()
        q.enqueue(current_node)
        while q.get_size() > 0:
            current_node = q.dequeue()
            for nbr in current_node.get_nbrs():
                nbr_node = self.get_node(nbr)
                if nbr_node.get_colour() == 'white':
                    nbr_node.set_colour('grey')
                    nbr_node.set_pred(current_node)
                    q.enqueue(nbr_node)
            current_node.set_colour('black')
            g.add_node(current_node.get_key())
            if current_node.get_pred():
                g.add_edge(current_node.get_pred().get_key(), current_node.get_key(), 0)
        return g

    def bfs(self):
        tree_list = []
        for node in self:
            if node.get_colour() == 'white':
                spanning_tree = self._bfs_visit(node)
                tree_list.append(spanning_tree)
        return tree_list
                
    def _dfs_visit(self, current_node):
        s = Stack()
        g = Graph()
        s.enqueue(current_node)
        current_node.set_colour('grey')
        g.add_node(current_node.get_key())
        while s.get_size() > 0:
            current_node = s.peek()
            all_done = True
            for nbr in current_node.get_nbrs():
                nbr_node = self.get_node(nbr)
                if nbr_node.get_colour() == 'white':
                    all_done = False
                    s.enqueue(nbr_node)
                    nbr_node.set_colour('grey')
                    g.add_node(nbr_node.get_key())
                    g.add_edge(current_node.get_key(), nbr_node.get_key(), 0)
                    break
            if all_done:
                current_node.set_colour('black')
                s.dequeue()

        return g

    def dfs(self):
        tree_list = []
        for node in self:
            if node.get_colour() == 'white':
                spanning_tree = self._dfs_visit(node)
                tree_list.append(spanning_tree)
        return tree_list
                
    def _top_dfs_visit(self, current_node):
        order_list = []
        s = Stack()
        s.enqueue(current_node)
        current_node.set_colour('grey')
        while s.get_size() > 0:
            current_node = s.peek()
            all_done = True
            for nbr in current_node.get_nbrs():
                nbr_node = self.get_node(nbr)
                if nbr_node.get_colour() == 'white':
                    all_done = False
                    s.enqueue(nbr_node)
                    nbr_node.set_colour('grey')
                    break
            if all_done:
                current_node.set_colour('black')
                s.dequeue()
                order_list.append(current_node)

        return order_list

    def topological_sort(self):
        top_list = []
        for node in self:
            if node.get_colour() == 'white':
                order_list = self._top_dfs_visit(node)
                top_list = top_list + order_list

        return [i for i in reversed(top_list)]

    def __contains__(self, key):
        return key in self.node_list

    def __iter__(self):
        return iter(self.node_list.values())


if __name__ == '__main__':
    g = Graph()
    # g.add_node('a')
    # g.add_node('b')
    # g.add_node('c')
    # g.add_node('d')
    # g.add_node('e')
    # g.add_node('f')
    # g.add_node('g')
    # g.add_node('h')
    # g.add_node('i')
    # g.add_node('j')
    # g.add_node('k')
    #
    # g.add_edge('a', 'c', 0)
    # g.add_edge('b', 'c', 0)
    # g.add_edge('c', 'e', 0)
    # g.add_edge('e', 'd', 0)
    # g.add_edge('d', 'f', 0)
    # g.add_edge('e', 'f', 0)
    # g.add_edge('f', 'g', 0)
    # g.add_edge('g', 'h', 0)
    # g.add_edge('f', 'h', 0)
    # g.add_edge('h', 'i', 0)
    # g.add_edge('h', 'k', 0)
    # g.add_edge('k', 'j', 0)

    # spantree = g.dfs()
    # for i in spantree:
    #     for j in i:
    #         print(j)

    g.add_node('milk')
    g.add_node('egg')
    g.add_node('oil')
    g.add_node('mix')
    g.add_node('heat grill')
    g.add_node('heat syrup')
    g.add_node('pour')
    g.add_node('turn')
    g.add_node('eat')

    g.add_edge('milk', 'mix', 0)
    g.add_edge('egg', 'mix', 0)
    g.add_edge('oil', 'mix', 0)
    g.add_edge('mix', 'heat syrup', 0)
    g.add_edge('mix', 'pour', 0)
    g.add_edge('heat grill', 'pour', 0)
    g.add_edge('pour', 'turn', 0)
    g.add_edge('turn', 'eat', 0)
    g.add_edge('heat syrup', 'eat', 0)

    print([i.key for i in g.topological_sort()])



















