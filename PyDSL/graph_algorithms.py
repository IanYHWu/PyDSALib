from PyDSL.graph import Graph
from PyDSL.graph import Node
from PyDSL.priority_queue import MinPriorityQueue


class DistanceNode(Node):

    def __init__(self, key):
        super().__init__(key)
        self.distance = 0
        self.pred = None

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_pred(self, node):
        self.pred = node

    def get_pred(self):
        return self.pred


def dijkstra(graph, dest_node):
    d_graph = Graph()
    for node in graph:
        d_node = DistanceNode(node.get_key())
        for nbr in node.get_nbrs():
            nbr_weight = node.get_weight(nbr)
            d_node.add_nbr(nbr, nbr_weight)
        d_node.set_distance(float('inf'))
        d_graph.node_list[d_node.get_key()] = d_node
        if node == dest_node:
            d_dest_node = d_node

    pq = MinPriorityQueue()
    d_dest_node.set_distance(0)
    pq.enqueue_list([(node.get_distance(), node) for node in d_graph])
    while pq.get_size() > 0:
        current_node = pq.dequeue().get_data()[1]
        for nbr in current_node.get_nbrs():
            nbr_node = d_graph.get_node(nbr)
            new_dist = current_node.get_distance() + current_node.get_weight(nbr)
            if new_dist < nbr_node.get_distance():
                nbr_node.set_distance(new_dist)
                nbr_node.set_pred(current_node)
                pq.change_val(nbr_node, new_dist)

    return d_graph


def prim(graph):
    d_graph = Graph()
    span_forest = []

    for node in graph:
        d_node = DistanceNode(node.get_key())
        for nbr in node.get_nbrs():
            nbr_weight = node.get_weight(nbr)
            d_node.add_nbr(nbr, nbr_weight)
        d_node.set_distance(float('inf'))
        d_graph.node_list[d_node.get_key()] = d_node

    pq = MinPriorityQueue()
    pq.enqueue_list([(node.get_distance(), node) for node in d_graph])
    last_node = None

    while pq.get_size() > 0:
        current_node = pq.dequeue().get_data()[1]
        if last_node and current_node.get_distance() != float('inf'):
            span_tree.add_node(current_node.get_key())
            span_tree.add_undirected_edge(last_node.get_key(), current_node.get_key(),
                                          last_node.get_weight(current_node.get_key()))
        elif current_node.get_distance() == float('inf'):
            span_forest.append(span_tree)
            span_tree = Graph()
            current_node.set_distance(0)
            span_tree.add_node(current_node.get_key())
        else:
            span_tree.add_node(current_node.get_key())
        for nbr in current_node.get_nbrs():
            nbr_node = d_graph.get_node(nbr)
            new_dist = current_node.get_weight(nbr)
            if nbr_node in pq and new_dist < nbr_node.get_distance():
                nbr_node.set_distance(new_dist)
                pq.change_val(nbr_node, new_dist)
        last_node = current_node

    span_forest.append(span_tree)

    return span_forest


# def traverse(start, graph):
#     x = graph.get_node(start)
#     print(x.get_key())
#     while x.get_pred():
#         print(x.get_pred().get_key())
#         x = x.get_pred()


if __name__ == '__main__':
        g = Graph()
        g.add_node('u')
        g.add_node('x')
        g.add_node('v')
        g.add_node('w')
        g.add_node('y')
        g.add_node('z')

        g.add_edge('u', 'v', 2)
        g.add_edge('u', 'x', 1)
        g.add_edge('u', 'w', 5)
        g.add_edge('w', 'u', 5)
        g.add_edge('x', 'u', 1)
        g.add_edge('v', 'u', 2)

        g.add_edge('x', 'v', 2)
        g.add_edge('v', 'x', 2)
        g.add_edge('x', 'w', 3)
        g.add_edge('w', 'x', 3)
        g.add_edge('v', 'w', 3)
        g.add_edge('w', 'v', 3)

        g.add_edge('x', 'y', 1)
        g.add_edge('y', 'x', 1)
        g.add_edge('y', 'w', 1)
        g.add_edge('w', 'y', 1)
        g.add_edge('y', 'z', 1)
        g.add_edge('z', 'y', 1)

        g.add_edge('w', 'z', 5)
        g.add_edge('z', 'w', 5)

        start_node = g.get_node('u')

        d_g = dijkstra(g, start_node)
        # traverse('w', d_g)
        print(d_g)

    # g = Graph()
    # g.add_node('A')
    # g.add_node('B')
    # g.add_node('C')
    # g.add_node('D')
    # g.add_node('E')
    # g.add_node('F')
    # g.add_node('G')
    #
    # g.add_undirected_edge('A', 'E', 1)
    # g.add_undirected_edge('A', 'B', 3)
    # g.add_undirected_edge('B', 'C', 9)
    # g.add_undirected_edge('B', 'D', 2)
    # g.add_undirected_edge('B', 'E', 2)
    # g.add_undirected_edge('C', 'D', 3)
    # g.add_undirected_edge('C', 'E', 7)
    # g.add_undirected_edge('F', 'G', 6)
    #
    # minspan = prim(g)
    # print(minspan)
    # for i in minspan:
    #     for j in i:
    #         print(j)

