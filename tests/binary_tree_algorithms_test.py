import unittest
from PyDSALib.binary_tree_algorithms import *
from PyDSALib.AVL_tree import AVLTree


class MyTestCase(unittest.TestCase):
    @staticmethod
    def setup():
        tree = AVLTree()
        key_list = [43, 55, 22, 15, 9]
        val_list = ['Penguin', 'Ant', 'Bear', 'Shark', 'Lion']
        for i, j in zip(key_list, val_list):
            tree[i] = j

        return tree

    def test_bfs(self):
        tree = self.setup()
        bfs_list = bfs(tree)
        true_results = [43, 15, 55, 9, 22]
        correct = True
        for i, j in zip(bfs_list, true_results):
            if i.get_key() != j:
                correct = False
            if not correct:
                break
        self.assertEqual(correct, True)

    def test_preorder(self):
        tree = self.setup()
        preorder_list = preorder(tree)
        true_results = [43, 15, 9, 22, 55]
        correct = True
        for i, j in zip(preorder_list, true_results):
            if i.get_key() != j:
                correct = False
            if not correct:
                break
        self.assertEqual(correct, True)

    def test_inorder(self):
        tree = self.setup()
        inorder_list = inorder(tree)
        true_results = [9, 15, 22, 43, 55]
        correct = True
        for i, j in zip(inorder_list, true_results):
            if i.get_key() != j:
                correct = False
            if not correct:
                break
        self.assertEqual(correct, True)

    def test_postorder(self):
        tree = self.setup()
        postorder_list = postorder(tree)
        true_results = [9, 22, 15, 55, 43]
        correct = True
        for i, j in zip(postorder_list, true_results):
            if i.get_key() != j:
                correct = False
            if not correct:
                break
        self.assertEqual(correct, True)


if __name__ == '__main__':
    unittest.main()
