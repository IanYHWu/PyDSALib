from PyDSL.graph import Graph
from PyDSL.graph import Node
from PyDSL.priority_queue import MinPriorityQueue
from PyDSL.queue import Queue
from PyDSL.stack import Stack


class DistanceNode(Node):
    """Node class for graph algorithms requiring distance and predecessor attributes. Extends the graph node class

        Attributes:
            key: key of the node
            connections: a dictionary containing the neighbours of the node and the weight of the edge as a key-val pair
            colour: flag for search algorithms. Default = 'white'
            distance: the distance attribute. Default = 0
            pred: the predecessor node. Default = None
        """

    def __init__(self, key):
        """Initialise the graph DistanceNode object

            Parameters:
                key: the key of the DistanceNode
            """
        super().__init__(key)
        self.distance = 0
        self.pred = None

    def set_distance(self, dist):
        """Set the distance of the node"""
        self.distance = dist

    def get_distance(self):
        """Get the distance of the node"""
        return self.distance

    def set_pred(self, node):
        """Set the predecessor node of the node"""
        self.pred = node

    def get_pred(self):
        """Get the predecessor node of the node"""
        return self.pred


def dijkstra(graph, start_node):
    """Perform Dijkstra's Algorithm on the graph, given a starting node.

        Parameters:
            graph: the graph to perform Dijkstra on
            start_node: the starting node, relative to which distances are found

        Returns:
            Returns a graph of DistanceNode objects, with the predecessor of each node corresponding
            to the shortest path from said node to the starting node
    """

    # initialise an empty graph, to replicate input graph but with DistanceNodes instead of Nodes
    d_graph = Graph()
    d_start_node = None
    for node in graph:
        # create DistanceNode
        d_node = DistanceNode(node.get_key())
        for nbr in node.get_nbrs():
            # connect new DistanceNode to all its neighbours
            nbr_weight = node.get_weight(nbr)
            d_node.add_nbr(nbr, nbr_weight)
        # set the node distance to infinity
        d_node.set_distance(float('inf'))
        # place DistanceNode into new graph
        d_graph.node_list[d_node.get_key()] = d_node
        # set the starting DistanceNode
        if node == start_node:
            d_start_node = d_node

    pq = MinPriorityQueue()
    # set the start node distance to 0 and enqueue all the nodes in the graph
    d_start_node.set_distance(0)
    # place tuple of (node distance, node) into priority queue - this will prioritise based on node distance
    pq.enqueue_list([(node.get_distance(), node) for node in d_graph])
    while pq.get_size() > 0:
        current_node = pq.dequeue().get_data()[1]
        # if the current_node has distance = inf, the node is in a disconnected portion of the graph. Stop searching
        if current_node.get_distance() == float('inf'):
            break
        for nbr in current_node.get_nbrs():
            # look through neighbours of current_node,
            # and set new distance = current_node distance + edge weight
            nbr_node = d_graph.get_node(nbr)
            new_dist = current_node.get_distance() + current_node.get_weight(nbr)
            if new_dist < nbr_node.get_distance():
                # if the new distance is less than the original neighbour node distance, set the current_node as
                # its predecessor and set its distance as new_dist.
                nbr_node.set_distance(new_dist)
                nbr_node.set_pred(current_node)
                # change the key of the node in the priority queue to reflect the new distance
                pq.change_key(nbr_node, new_dist)

    return d_graph


def prim(graph):
    """Performs Prim's Algorithm on the graph.

        Parameters:
            graph: the graph to find the MST of a graph

        Returns:
            A list of minimum spanning trees (graphs)
    """

    # initialise an empty graph, to replicate input graph but with DistanceNodes instead of Nodes
    d_graph = Graph()
    span_tree = None
    span_forest = []

    for node in graph:
        # convert nodes in the graph to DistanceNodes
        d_node = DistanceNode(node.get_key())
        for nbr in node.get_nbrs():
            nbr_weight = node.get_weight(nbr)
            d_node.add_nbr(nbr, nbr_weight)
        # set the distances of all nodes to inf
        d_node.set_distance(float('inf'))
        # put node into the new graph
        d_graph.node_list[d_node.get_key()] = d_node

    pq = MinPriorityQueue()
    # place tuple of (node distance, node) into priority queue - this will prioritise based on node distance
    pq.enqueue_list([(node.get_distance(), node) for node in d_graph])
    last_node = None

    while pq.get_size() > 0:
        current_node = pq.dequeue().get_data()[1]
        if last_node and current_node.get_distance() != float('inf'):
            # add the new node to the spanning tree and connect to the last node
            span_tree.add_node(current_node.get_key())
            span_tree.add_undirected_edge(last_node.get_key(), current_node.get_key(),
                                          last_node.get_weight(current_node.get_key()))
        elif current_node.get_distance() == float('inf'):
            # if the current node has distance = inf, start a new spanning tree and set dist = 0
            span_forest.append(span_tree)
            span_tree = Graph()
            current_node.set_distance(0)
            span_tree.add_node(current_node.get_key())
        else:
            # if not last node and dist != inf, just add the node
            span_tree.add_node(current_node.get_key())
        for nbr in current_node.get_nbrs():
            # get the node and the edge weight to each neighbour
            nbr_node = d_graph.get_node(nbr)
            new_dist = current_node.get_weight(nbr)
            if nbr_node in pq and new_dist < nbr_node.get_distance():
                # set the neighbour distance as the weight between current_node and neighbour
                nbr_node.set_distance(new_dist)
                # change the key of the node in the priority queue to reflect the new distance
                pq.change_key(nbr_node, new_dist)
        last_node = current_node

    span_forest.append(span_tree)

    return span_forest


def _bfs_visit(graph, current_node):
    """Helper method for graph breadth-first search"""
    q = Queue()
    g = Graph()  # initialise the spanning tree
    q.enqueue(current_node)
    while q.get_size() > 0:
        current_node = q.dequeue()
        # add the new node to the spanning tree
        g.add_node(current_node.get_key())
        # set the colour to black after adding to tree
        current_node.set_colour('black')
        for nbr in current_node.get_nbrs():
            # get the neighbour nodes
            nbr_node = graph.get_node(nbr)
            if nbr_node.get_colour() == 'white':
                # if the neighbour node is unexplored (white), set to waiting (grey)
                nbr_node.set_colour('grey')
                # add edge between current node and neighbour. Then put neighbour in queue
                g.add_edge(current_node.get_key(), nbr_node.get_key(), current_node.get_weight(nbr))
                q.enqueue(nbr_node)

    return g


def bfs(graph):
    """Perform breadth-first search on the graph.

        Parameters:
            graph: the graph to perform BFS on

        Returns:
            Returns a list of spanning trees (graphs)
    """

    tree_list = []  # initialise forest (list of trees)
    # search through graph and call bfs on all unexplored nodes. Append to forest
    for node in graph:
        if node.get_colour() == 'white':
            spanning_tree = _bfs_visit(graph, node)
            tree_list.append(spanning_tree)
    return tree_list


def _dfs_visit(graph, current_node):
    """Helper method for graph depth-first search"""
    s = Stack()
    g = Graph()  # initialise the spanning tree
    s.push(current_node)
    current_node.set_colour('grey')
    # add the current_node to the spanning tree
    g.add_node(current_node.get_key())
    while s.get_size() > 0:
        current_node = s.peek()
        all_done = True  # flag for all neighbours in waiting
        for nbr in current_node.get_nbrs():
            nbr_node = graph.get_node(nbr)
            if nbr_node.get_colour() == 'white':
                all_done = False  # if neighbour is unexplored, set flag to false
                s.push(nbr_node)
                nbr_node.set_colour('grey')
                # add neighbour node to the graph and connect current_node and the neighbour
                g.add_node(nbr_node.get_key())
                g.add_edge(current_node.get_key(), nbr_node.get_key(), current_node.get_weight(nbr))
                break  # escape from the current node, select a new node from the stack
        if all_done:
            # remove the node from stack once all neighbours are in waiting
            current_node.set_colour('black')
            s.pop()

    return g


def dfs(graph):
    """Perform depth-first search on the graph.

           Parameters:
               graph: the graph to perform DFS on

           Returns:
               Returns a list of spanning trees (graphs)
    """
    tree_list = []  # initialise forest (list of trees)
    for node in graph:
        # search through graph and call dfs on all unexplored nodes. Append to forest
        if node.get_colour() == 'white':
            spanning_tree = _dfs_visit(graph, node)
            tree_list.append(spanning_tree)
    return tree_list


def _top_dfs_visit(graph, current_node):
    """Helper method for topological sort"""
    order_list = []
    s = Stack()
    s.push(current_node)
    current_node.set_colour('grey')
    while s.get_size() > 0:
        current_node = s.peek()
        all_done = True  # flag for all neighbours in waiting
        for nbr in current_node.get_nbrs():
            nbr_node = graph.get_node(nbr)
            if nbr_node.get_colour() == 'white':
                all_done = False  # if one of the neighbours is unexplored, set flag as false
                # add the neighbour to the stack and then set neighbour to in waiting
                s.push(nbr_node)
                nbr_node.set_colour('grey')
                break  # escape from the current node, select a new node from the stack
        if all_done:
            # remove the node from stack once all neighbours are in waiting
            current_node.set_colour('black')
            s.pop()
            order_list.append(current_node)  # place the node in the order_list

    return order_list


def topological_sort(graph):
    """Performs topological sort on a directed acyclic graph.

        Parameters:
            graph: the graph to perform topological sort on

        Returns:
            A list of sorted nodes
    """

    top_list = []
    for node in graph:
        # search through graph and call topological sort on all unexplored nodes
        if node.get_colour() == 'white':
            order_list = _top_dfs_visit(graph, node)
            # combine the lists
            top_list = top_list + order_list

    return [i for i in reversed(top_list)]


if __name__ == '__main__':
    g = Graph()
#         g.add_node('u')
#         g.add_node('x')
#         g.add_node('v')
#         g.add_node('w')
#         g.add_node('y')
#         g.add_node('z')
#         g.add_node('a')
#         g.add_node('b')
#
#         g.add_edge('u', 'v', 2)
#         g.add_edge('u', 'x', 1)
#         g.add_edge('u', 'w', 5)
#         g.add_edge('w', 'u', 5)
#         g.add_edge('x', 'u', 1)
#         g.add_edge('v', 'u', 2)
#
#         g.add_edge('x', 'v', 2)
#         g.add_edge('v', 'x', 2)
#         g.add_edge('x', 'w', 3)
#         g.add_edge('w', 'x', 3)
#         g.add_edge('v', 'w', 3)
#         g.add_edge('w', 'v', 3)
#
#         g.add_edge('x', 'y', 1)
#         g.add_edge('y', 'x', 1)
#         g.add_edge('y', 'w', 1)
#         g.add_edge('w', 'y', 1)
#         g.add_edge('y', 'z', 1)
#         g.add_edge('z', 'y', 1)
#
#         g.add_edge('w', 'z', 5)
#         g.add_edge('z', 'w', 5)
#
#         g.add_edge('a', 'b', 2)
#
#         start_node = g.get_node('u')
#
#         d_g = dijkstra(g, start_node)
#         print(d_g)
#
#         dest_node = d_g.get_node('w')
#         x = dest_node
#         print(x.key)
#         while x.pred:
#             print(x.pred.key)
#             x = x.pred


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
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')
    g.add_node('g')
    g.add_node('h')
    g.add_node('i')
    g.add_node('j')
    g.add_node('k')

    g.add_undirected_edge('a', 'c', 3)
    g.add_undirected_edge('b', 'c', 0)
    g.add_undirected_edge('c', 'e', 4)
    g.add_undirected_edge('e', 'd', 0)
    g.add_undirected_edge('d', 'f', 1)
    g.add_undirected_edge('e', 'f', 9)
    g.add_undirected_edge('f', 'g', 3)
    g.add_undirected_edge('g', 'h', 0)
    g.add_undirected_edge('f', 'h', 7)
    g.add_undirected_edge('h', 'i', 6)
    g.add_undirected_edge('h', 'k', 3)
    g.add_undirected_edge('k', 'j', 0)

    spantree = dfs(g)
    for i in spantree:
        for j in i:
            print(j)
