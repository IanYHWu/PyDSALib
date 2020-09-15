
from PyDSL.queue import Queue


class TreeNode:
    """Node class for binary tree

    Attributes:
        key: key of the node
        val: value of the node
        left_child: TreeNode object. The left child of the current node
        right_child: TreeNode object. The right child of the current node
        parent: TreeNode object. The parents of the current node
    """

    def __init__(self, key, val, left_child=None, right_child=None, parent=None):
        """Initialises the TreeNode object

            Arguments:
                key: key of the root node
                val: value of the root node
                left_child: TreeNode object. The left child of the current node (default = None)
                right_child: TreeNode object. The right child of the current node (default = None)
                parent: TreeNode object. The parent of the current node (default = None)
        """
        self.key = key
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def get_left_child(self):
        """Getter method for the left child"""
        return self.left_child

    def get_right_child(self):
        """Getter method for the right child"""
        return self.right_child

    def is_leaf(self):
        """Check if the current node is a leaf"""
        return not self.left_child and not self.right_child

    def has_left_child_only(self):
        """Check if the current node has a left child only"""
        return self.left_child and not self.right_child

    def has_right_child_only(self):
        """Check if the current node has a right child only"""
        return self.right_child and not self.left_child

    def get_successor(self):
        """Calls find_min() to get the successor node"""
        return self.right_child.find_min()

    def find_min(self):
        """Finds the node with minimum key in the tree"""
        current_node = self
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node

    def splice(self):
        """Splices out a node"""
        if self.right_child:
            self.parent.left_child = self.right_child
        else:
            self.parent.left_child = None

    def __iter__(self):
        if self:
            if self.get_left_child():
                for i in self.left_child:
                    yield i
            yield self.key
            if self.get_right_child():
                for i in self.right_child:
                    yield i


class BinaryTree:
    """Binary tree class

        Attributes:
            root: the root node of the tree (default = None)
            size: the number of elements in the binary tree (default = 0)

    """

    def __init__(self):
        """Initialises the binary tree"""
        self.root = None
        self.size = 0

    def get_size(self):
        """Getter method for size"""
        return self.size

    def put(self, key, val):
        """Inserts a new node into the tree at the correct location"""
        if self.root:
            self._put(key, val, self.root)
            self.size += 1
        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, current_node):
        """Helper method for put"""
        if key < current_node.key:
            if current_node.get_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        elif key > current_node.key:
            if current_node.get_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
        else:
            current_node.val = val

    def get(self, key):
        """Returns the value of the node with a matching key"""
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.val
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """Helper method for get"""
        if not current_node:
            return None
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        elif current_node.key < key:
            return self._get(key, current_node.right_child)
        elif current_node.key == key:
            return current_node

    def delete(self, key):
        """Deletes a node with matching key"""
        if self.size > 1:
            result = self._get(key, self.root)
            if result:
                self._remove_node(result)
                self.size -= 1
            else:
                print('Error! {} not found in Tree'.format(key))
        elif self.get_size() == 1:
            if self.root.key == key:
                self.root = None
                self.size -= 1
            else:
                print('Error! {} not found in Tree'.format(key))
        else:
            print('Error! {} not found in Tree'.format(key))

    @staticmethod
    def _remove_node(node):
        """Helper method for delete"""
        if node.is_leaf():
            if node.parent.left_child == node:
                node.parent.left_child = None
            elif node.parent.right_child == node:
                node.parent.right_child = None
        elif node.has_left_child_only():
            if node.parent.left_child == node:
                node.parent.left_child = node.left_child
            elif node.parent.right_child == node:
                node.parent.right_child = node.left_child
        elif node.has_right_child_only():
            if node.parent.left_child == node:
                node.parent.left_child = node.right_child
            elif node.parent.right_child == node:
                node.parent.right_child = node.right_child
        else:
            succ = node.get_successor()
            succ.splice()
            node.key = succ.key
            node.val = succ.val

    def get_height(self, key):
        """Calculates and returns the height of a node with matching key. Root height = 0"""
        current_node = self._get(key, self.root)
        height_counter = 0
        while current_node.parent:
            current_node = current_node.parent
            height_counter += 1
        return height_counter

    def bfs(self):
        """Implements breadth-first search of the tree. Returns a list of nodes in order of the search"""
        bfs_list = []
        node_queue = Queue()
        node_queue.enqueue(self.root)
        while not node_queue.is_empty():
            current_node = node_queue.dequeue()
            if current_node.get_left_child():
                node_queue.enqueue(current_node.get_left_child())
            if current_node.get_right_child():
                node_queue.enqueue(current_node.get_right_child())
            bfs_list.append(current_node)

        return bfs_list

    def preorder(self, current_node=None, order_list=[], root_set=False):
        """Implements preorder traversal of the tree. Returns a list of nodes in order of the search"""
        if not current_node and not root_set:
            root_set = True
            current_node = self.root
        if current_node:
            order_list.append(current_node)
            self.preorder(current_node=current_node.get_left_child(), root_set=root_set)
            self.preorder(current_node=current_node.get_right_child(), root_set=root_set)

        return order_list

    def inorder(self, current_node=None, order_list=[], root_set=False):
        """Implements inorder traversal of the tree. Returns a list of nodes in order of the search"""
        if not current_node and not root_set:
            root_set = True
            current_node = self.root
        if current_node:
            self.inorder(current_node=current_node.get_left_child(), root_set=root_set)
            order_list.append(current_node)
            self.inorder(current_node=current_node.get_right_child(), root_set=root_set)

        return order_list

    def postorder(self, current_node=None, order_list=[], root_set=False):
        """Implements postorder traversal of the tree. Returns a list of nodes in order of the search"""
        if not current_node and not root_set:
            root_set = True
            current_node = self.root
        if current_node:
            self.postorder(current_node=current_node.get_left_child(), root_set=root_set)
            self.postorder(current_node=current_node.get_right_child(), root_set=root_set)
            order_list.append(current_node)

        return order_list

    def __setitem__(self, key, val):
        self.put(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)


# if __name__ == '__main__':
#     tree = BinaryTree()
#     # key_list = [43, 55, 22, 15, 98, 1, 34, 76]
#     key_list = [1, 2, 3, 4, 5, 6, 7, 8]
#     val_list = ['Penguin', 'Ant', 'Bear', 'Shark', 'Eagle', 'Dog', 'Cat', 'Turtle']
#
#     for i, j in zip(key_list, val_list):
#         tree[i] = j
#
#     sortedtree = tree.bfs()
#     print('+++++++')
#     for node in sortedtree:
#         print(node.key)
