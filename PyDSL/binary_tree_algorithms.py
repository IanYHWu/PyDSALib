from PyDSL.binary_tree import BinaryTree
from PyDSL.queue import Queue


def bfs(tree):
    """Perform breadth-first search of the tree.

    Parameters:
        tree: the tree to perform BFS on

    Returns:
        A list of nodes in order of the search
    """
    bfs_list = []
    node_queue = Queue()
    node_queue.enqueue(tree.root)
    while not node_queue.is_empty():
        # get the node first-in first-out
        current_node = node_queue.dequeue()
        # get the children and place into queue
        if current_node.get_left_child():
            node_queue.enqueue(current_node.get_left_child())
        if current_node.get_right_child():
            node_queue.enqueue(current_node.get_right_child())
        # attach node to list
        bfs_list.append(current_node)

    return bfs_list


def _preorder(tree, current_node=None, order_list=[], root_set=False):
    """Helper method to implement preorder traversal of the tree"""
    # find the root and set as current_node for first iteration
    if not current_node and not root_set:
        root_set = True
        current_node = tree.root
    if current_node:
        # search the tree recursively and append the nodes to order_list in preorder fashion
        order_list.append(current_node)
        _preorder(tree, current_node=current_node.get_left_child(), root_set=root_set)
        _preorder(tree, current_node=current_node.get_right_child(), root_set=root_set)

    return order_list


def preorder(tree):
    """Perform preorder tree traversal.

        Parameters:
            tree: the tree to perform preorder traversal on

        Returns:
            A list of nodes in order of the search
    """
    return _preorder(tree)


def _inorder(tree, current_node=None, order_list=[], root_set=False):
    """Helper method to implement inorder traversal of the tree"""
    if not current_node and not root_set:
        # find the root and set as current_node for first iteration
        root_set = True
        current_node = tree.root
    if current_node:
        # search the tree recursively and append the nodes to order_list in inorder fashion
        _inorder(tree, current_node=current_node.get_left_child(), root_set=root_set)
        order_list.append(current_node)
        _inorder(tree, current_node=current_node.get_right_child(), root_set=root_set)

    return order_list


def inorder(tree):
    """Perform inorder tree traversal.

        Parameters:
            tree: the tree to perform inorder traversal on

        Returns:
            A list of nodes in order of the search
    """
    return _inorder(tree)


def _postorder(tree, current_node=None, order_list=[], root_set=False):
    """Helper method to implement postorder traversal of the tree"""
    if not current_node and not root_set:
        # find the root and set as current_node for first iteration
        root_set = True
        current_node = tree.root
    if current_node:
        # search the tree recursively and append the nodes to order_list in postorder fashion
        _postorder(tree, current_node=current_node.get_left_child(), root_set=root_set)
        _postorder(tree, current_node=current_node.get_right_child(), root_set=root_set)
        order_list.append(current_node)

    return order_list


def postorder(tree):
    """Perform postorder tree traversal.

        Parameters:
            tree: the tree to perform postorder traversal on

        Returns:
            A list of nodes in order of the search
    """
    return _postorder(tree)


if __name__ == '__main__':
    tree = BinaryTree()
    key_list = [43, 55, 22, 15, 98, 1, 34, 76]
    val_list = ['Penguin', 'Ant', 'Bear', 'Shark', 'Eagle', 'Dog', 'Cat', 'Turtle']

    for i, j in zip(key_list, val_list):
        tree[i] = j

    print(tree[43].get_val())
    print(43 in tree)

    print([i.get_val() for i in preorder(tree)])
    print([i.get_val() for i in inorder(tree)])
    print([i.get_val() for i in postorder(tree)])
    print([i.get_val() for i in bfs(tree)])






