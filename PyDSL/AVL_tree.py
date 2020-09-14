
from PyDSL.binary_tree import BinaryTree
from PyDSL.binary_tree import TreeNode


class AVLNode(TreeNode):
   
    def __init__(self, key, val, left_child=None, right_child=None, parent=None):
        super().__init__(key, val, left_child, right_child, parent)
        self.balance_factor = 0
        

class AVLTree(BinaryTree):

    def __init__(self):
        super().__init__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
            self.size += 1
        else:
            self.root = AVLNode(key, val)
            self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.get_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = AVLNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        elif key > current_node.key:
            if current_node.get_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = AVLNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        print("updating")
        print("node: {}".format(node.parent))

        if node.balance_factor > 1 or node.balance_factor < -1:
            print("there")
            self.rebalance(node)
            return
        if node.parent:
            print("here")
            if node.parent.left_child == node:
                node.parent.balance_factor += 1
            elif node.parent.right_child == node:
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, org_root):

        new_root = org_root.right_child
        org_root.right_child = new_root.left_child
        if new_root.left_child:
            new_root.left_child.parent = org_root
        new_root.parent = org_root.parent
        if not org_root.parent:
            self.root = new_root
        else:
            if org_root.parent.left_child == org_root:
                org_root.parent.left_child = new_root
            elif org_root.parent.right_child == org_root:
                org_root.parent.right_child = new_root
        new_root.left_child = org_root
        org_root.parent = new_root
        org_root.balance_factor = org_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(org_root.balance_factor, 0)

    def rotate_right(self, org_root):

        new_root = org_root.left_child
        org_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = org_root
        new_root.parent = org_root.parent
        if not org_root.parent:
            self.root = new_root
        else:
            if org_root.parent.left_child == org_root:
                org_root.parent.left_child = new_root
            elif org_root.parent.right_child == org_root:
                org_root.parent.right_child = new_root
        new_root.right_child = org_root
        org_root.parent = new_root
        org_root.balance_factor = org_root.balance_factor - 1 + min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 - max(org_root.balance_factor, 0)

    def rebalance(self, node):
        print("rebalancing")

        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)


if __name__ == '__main__':
    avltree = AVLTree()
    key_list = [43, 55, 22, 15, 98, 1, 34, 76, 2, 3]
    val_list = ['Penguin', 'Ant', 'Bear', 'Shark', 'Eagle', 'Dog', 'Cat', 'Turtle', 'Lion', 'Fish']

    for i, j in zip(key_list, val_list):
        print('Inserting {}'.format(i))
        avltree[i] = j

    avl_height_list = []
    for i in key_list:
        print(i)
        avl_height_list.append(avltree.get_height(i))
    for i, j in zip(key_list, avl_height_list):
        print((i, j))

    print("+++++")
    sortedtree = avltree.bfs()
    for node in sortedtree:
        print(node.key)