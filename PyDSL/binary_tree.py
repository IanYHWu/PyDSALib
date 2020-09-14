
from PyDSL.queue import Queue


class TreeNode:

    def __init__(self, key, val, left_child=None, right_child=None, parent=None):
        self.key = key
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def is_leaf(self):
        return not self.left_child and not self.right_child

    def has_left_child_only(self):
        return self.left_child and not self.right_child

    def has_right_child_only(self):
        return self.right_child and not self.left_child

    def get_successor(self):
        return self.right_child.find_min()

    def find_min(self):
        current_node = self
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node

    def splice(self):
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

    def __init__(self):
        self.root = None
        self.size = 0

    def get_size(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
            self.size += 1
        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, current_node):
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
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.val
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        elif current_node.key < key:
            return self._get(key, current_node.right_child)
        elif current_node.key == key:
            return current_node

    def delete(self, key):
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
        current_node = self._get(key, self.root)
        height_counter = 0
        while current_node.parent:
            current_node = current_node.parent
            height_counter += 1
        return height_counter

    def bfs(self):
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
        if not current_node and not root_set:
            root_set = True
            current_node = self.root
        if current_node:
            order_list.append(current_node)
            self.preorder(current_node=current_node.get_left_child(), root_set=root_set)
            self.preorder(current_node=current_node.get_right_child(), root_set=root_set)

        return order_list

    def inorder(self, current_node=None, order_list=[], root_set=False):
        if not current_node and not root_set:
            root_set = True
            current_node = self.root
        if current_node:
            self.inorder(current_node=current_node.get_left_child(), root_set=root_set)
            order_list.append(current_node)
            self.inorder(current_node=current_node.get_right_child(), root_set=root_set)

        return order_list

    def postorder(self, current_node=None, order_list=[], root_set=False):
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


if __name__ == '__main__':
    tree = BinaryTree()
    # key_list = [43, 55, 22, 15, 98, 1, 34, 76]
    key_list = [1, 2, 3, 4, 5, 6, 7, 8]
    val_list = ['Penguin', 'Ant', 'Bear', 'Shark', 'Eagle', 'Dog', 'Cat', 'Turtle']

    for i, j in zip(key_list, val_list):
        tree[i] = j

    sortedtree = tree.bfs()
    print('+++++++')
    for node in sortedtree:
        print(node.key)
