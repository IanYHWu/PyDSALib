import unittest
from PyDSALib.AVL_tree import AVLTree


class MyTestCase(unittest.TestCase):
    @staticmethod
    def setup():
        tree = AVLTree()
        key_list = [1, 7, 22, 15]
        val_list = ['Penguin', 'Ant', 'Bear', 'Shark']
        for i, j in zip(key_list, val_list):
            tree[i] = j

        return tree

    def test_setup(self):
        tree = self.setup()
        root = tree.root
        self.assertEqual(root.get_key(), 7)
        self.assertEqual(root.get_val(), 'Ant')
        current_node = root.get_left_child()
        self.assertEqual(current_node.get_key(), 1)
        self.assertEqual(current_node.get_val(), 'Penguin')
        current_node = root.get_right_child()
        self.assertEqual(current_node.get_key(), 22)
        self.assertEqual(current_node.get_val(), 'Bear')
        current_node = current_node.get_left_child()
        self.assertEqual(current_node.get_key(), 15)
        self.assertEqual(current_node.get_val(), 'Shark')

    def test_insert_node(self):
        tree = self.setup()
        tree.insert_node(9, 'Lion')
        root = tree.root
        current_node = root.get_right_child()
        self.assertEqual(current_node.get_key(), 15)
        self.assertEqual(current_node.get_val(), 'Shark')
        current_node = current_node.get_left_child()
        self.assertEqual(current_node.get_key(), 9)
        self.assertEqual(current_node.get_val(), 'Lion')


if __name__ == '__main__':
    unittest.main()
