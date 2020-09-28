
class Node:
    """Node class for graphs

        Attributes:
            key: key of the node
            connections: a dictionary containing the neighbours of the node and the weight of the edge as a key-val pair
            colour: flag for search algorithms. Default = 'white'
    """

    def __init__(self, key):
        """Initialise the graph node object"""
        self.key = key
        self.connections = {}
        self.colour = 'white'

    def add_nbr(self, nbr, weight):
        """Add a neighbour, and specify the weight of the edge"""
        self.connections[nbr] = weight

    def get_nbrs(self):
        """Get the keys of all the neighbours in a list"""
        return self.connections.keys()

    def get_key(self):
        """Get the key of the node"""
        return self.key

    def get_weight(self, nbr):
        """Get the weight of the edge connecting the node and a neighbour"""
        return self.connections[nbr]

    def get_colour(self):
        """Get the colour of the node"""
        return self.colour

    def set_colour(self, col):
        """Set the colour of the node"""
        self.colour = col

    def __repr__(self):
        return 'Node {}: contains connections to {}'.format(self.key, self.connections)


class Graph:
    """Graph class

        Attributes:
            node_list: a list of all nodes belonging to the graph
            size: the number of nodes in the graph
    """

    def __init__(self):
        """Initialise an empty graph"""
        self.node_list = {}
        self.size = 0

    def add_node(self, key):
        """Add a node to the graph"""
        self.size += 1
        new_node = Node(key)
        self.node_list[key] = new_node
        return new_node

    def get_node(self, key):
        """Get the node in the graph with corresponding key"""
        if key in self.node_list:
            return self.node_list[key]
        else:
            return None

    def add_edge(self, key, edge, weight):
        """Add an edge between two nodes (from key to edge) with specified weight"""
        target = self.get_node(key)
        if target:
            # add edge from Node(key) to Node(edge)
            target.add_nbr(edge, weight)
        else:
            return 'Cannot add edge. Selected node does not exist'

    def add_undirected_edge(self, key, edge, weight):
        """Add an undirected edge between two nodes (from key to edge) with specified weight"""
        target = self.get_node(key)
        targeted = self.get_node(edge)
        if target and targeted:
            # add edge from Node(key) to Node(edge)
            target.add_nbr(edge, weight)
            # add edge from Node(edge) to Node(key)
            targeted.add_nbr(key, weight)
        else:
            return 'Cannot add undirected edge. One of the selected nodes does not exist'

    def get_nodes(self):
        """Get the keys of all the nodes in the graph"""
        return self.node_list.keys()

    def __contains__(self, key):
        return key in self.node_list

    def __iter__(self):
        return iter(self.node_list.values())












