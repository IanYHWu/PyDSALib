import unittest
from PyDSALib.binary_tree import BinaryTree


class BinaryTreeTest(unittest.TestCase):

    @staticmethod
    def setup():
        tree = BinaryTree()
        key_list = [43, 55, 22, 15]
        val_list = ['Penguin', 'Ant', 'Bear', 'Shark']
        for i, j in zip(key_list, val_list):
            tree[i] = j

        return tree

    def test_setup(self):
        tree = self.setup()
        root = tree.root
        self.assertEqual(root.get_key(), 43)
        self.assertEqual(root.get_val(), 'Penguin')
        current_node = root.get_left_child()
        self.assertEqual(current_node.get_key(), 22)
        self.assertEqual(current_node.get_val(), 'Bear')
        current_node = current_node.get_left_child()
        self.assertEqual(current_node.get_key(), 15)
        self.assertEqual(current_node.get_val(), 'Shark')
        current_node = root.get_right_child()
        self.assertEqual(current_node.get_key(), 55)
        self.assertEqual(current_node.get_val(), 'Ant')

    def test_insert_node(self):
        tree = self.setup()
        tree.insert_node(99, 'Lion')
        root = tree.root
        current_node = root.get_right_child().get_right_child()
        self.assertEqual(current_node.get_key(), 99)
        self.assertEqual(current_node.get_val(), 'Lion')

    def test_magic_insert_node(self):
        tree = self.setup()
        tree[99] = 'Lion'
        root = tree.root
        current_node = root.get_right_child().get_right_child()
        self.assertEqual(current_node.get_key(), 99)
        self.assertEqual(current_node.get_val(), 'Lion')

    def test_get_size(self):
        tree = self.setup()
        self.assertEqual(tree.get_size(), 4)

    def test_get_node(self):
        tree = self.setup()
        self.assertEqual(tree.get_node(22).get_val(), 'Bear')

    def test_magic_get_node(self):
        tree = self.setup()
        self.assertEqual(tree[22].get_val(), 'Bear')

    def test_del(self):
        tree = self.setup()
        tree.delete(22)
        root = tree.root
        self.assertEqual(root.get_key(), 43)
        self.assertEqual(root.get_val(), 'Penguin')
        current_node = root.get_left_child()
        self.assertEqual(current_node.get_key(), 15)
        self.assertEqual(current_node.get_val(), 'Shark')
        current_node = root.get_right_child()
        self.assertEqual(current_node.get_key(), 55)
        self.assertEqual(current_node.get_val(), 'Ant')

    def test_magic_del(self):
        tree = self.setup()
        del tree[22]
        root = tree.root
        self.assertEqual(root.get_key(), 43)
        self.assertEqual(root.get_val(), 'Penguin')
        current_node = root.get_left_child()
        self.assertEqual(current_node.get_key(), 15)
        self.assertEqual(current_node.get_val(), 'Shark')
        current_node = root.get_right_child()
        self.assertEqual(current_node.get_key(), 55)
        self.assertEqual(current_node.get_val(), 'Ant')

    def test_get_height(self):
        tree = self.setup()
        self.assertEqual(tree.get_height(55), 1)

    def test_magic_contains(self):
        tree = self.setup()
        self.assertEqual(22 in tree, True)
        self.assertEqual(20 in tree, False)


if __name__ == '__main__':
    unittest.main()
