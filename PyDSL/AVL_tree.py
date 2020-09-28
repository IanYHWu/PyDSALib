from PyDSL.binary_tree import BinaryTree
from PyDSL.binary_tree import TreeNode


class AVLNode(TreeNode):
    """Node class for AVL (self-balancing) tree. Extends the TreeNode class

        Attributes:
            key: key of the node
            val: value of the node
            left_child: TreeNode object. The left child of the current node
            right_child: TreeNode object. The right child of the current node
            parent: TreeNode object. The parents of the current node
            balance_factor: the balance factor of the node
    """

    def __init__(self, key, val, left_child=None, right_child=None, parent=None):
        """Initialise the AVLNode object

            Arguments:
                key: key of the root node
                val: value of the root node
                left_child: TreeNode object. The left child of the current node (default = None)
                right_child: TreeNode object. The right child of the current node (default = None)
                parent: TreeNode object. The parent of the current node (default = None)
        """
        super().__init__(key, val, left_child, right_child, parent)
        self.balance_factor = 0


class AVLTree(BinaryTree):
    """AVL tree class. Extends BinaryTree

        Attributes:
            root: the root node of the tree (default = None)
            size: the number of elements in the binary tree (default = 0)
    """
    def __init__(self):
        """Initialise the AVLTree object"""
        super().__init__()

    def insert_node(self, key, val):
        """Insert a new node into the tree at the correct location. Overrides insert_node method in BinaryTree"""
        if self.root:
            self._put(key, val, self.root)
            self.size += 1
        else:
            self.root = AVLNode(key, val)
            self.size += 1

    def _put(self, key, val, current_node):
        """Helper method for insert_node. Overrides _put method in BinaryTree"""
        if key < current_node.key:
            if current_node.get_left_child():
                # if current_node has a left child and key < current key, recursively call _put to continue searching
                self._put(key, val, current_node.left_child)
            else:
                # if current node does not have a left child, insert node as left child and update balanace
                current_node.left_child = AVLNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.get_right_child():
                # if current_node has a right child and key >= current key, recursively call _put to continue searching
                self._put(key, val, current_node.right_child)
            else:
                # if current node does not have a right child, insert node as right child and update balance
                current_node.right_child = AVLNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        """Update the balance factor of every node, and rebalance the tree if necessary"""
        if node.balance_factor > 1 or node.balance_factor < -1:
            # call rebalance if the node is out of balance
            self.rebalance(node)
            return
        if node.parent:
            # adjust the parent balance
            if node.parent.left_child == node:
                node.parent.balance_factor += 1
            elif node.parent.right_child == node:
                node.parent.balance_factor -= 1
            # recursively update the parent if out of balance
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, org_root):
        """Implement left rotation of a node"""
        new_root = org_root.right_child
        org_root.right_child = new_root.left_child
        # locate the nodes to rotate
        if new_root.left_child:
            new_root.left_child.parent = org_root
        new_root.parent = org_root.parent
        # if root is rotated, set a new root for the tree
        if not org_root.parent:
            self.root = new_root
        else:
            if org_root.parent.left_child == org_root:
                org_root.parent.left_child = new_root
            elif org_root.parent.right_child == org_root:
                org_root.parent.right_child = new_root
        # perform rotation
        new_root.left_child = org_root
        org_root.parent = new_root
        # update the balance factors of parent and child
        org_root.balance_factor = org_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(org_root.balance_factor, 0)

    def rotate_right(self, org_root):
        """Implement right rotation of a node"""
        new_root = org_root.left_child
        org_root.left_child = new_root.right_child
        # locate the nodes to rotate
        if new_root.right_child:
            new_root.right_child.parent = org_root
        new_root.parent = org_root.parent
        # if root is rotated, set a new root for the tree
        if not org_root.parent:
            self.root = new_root
        else:
            if org_root.parent.left_child == org_root:
                org_root.parent.left_child = new_root
            else:
                org_root.parent.right_child = new_root
        # perform rotation
        new_root.right_child = org_root
        org_root.parent = new_root
        # update the balance factors of parent and child
        org_root.balance_factor = org_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(org_root.balance_factor, 0)

    def rebalance(self, node):
        """Rebalance the tree"""
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                # perform two rotations for a "crooked" branch
                self.rotate_right(node.right_child)  # straighten branch
                self.rotate_left(node)
                # perform a single rotation for a straight branch
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                # perform two rotations for a "crooked" branch
                self.rotate_left(node.left_child)  # straighten branch
                self.rotate_right(node)
                # perform a single rotation for a straight branch
            else:
                self.rotate_right(node)


# if __name__ == '__main__':
#     avltree = AVLTree()
#     key_list = [43, 55, 22, 15, 98, 1, 34, 76, 2, 3]
#     val_list = ['Penguin', 'Ant', 'Bear', 'Shark', 'Eagle', 'Dog', 'Cat', 'Turtle', 'Lion', 'Fish']
#
#     for i, j in zip(key_list, val_list):
#         print('Inserting {}'.format(i))
#         avltree[i] = j
#
#     avl_height_list = []
#     for i in key_list:
#         print(i)
#         avl_height_list.append(avltree.get_height(i))
#     for i, j in zip(key_list, avl_height_list):
#         print((i, j))
