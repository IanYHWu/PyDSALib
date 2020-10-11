import unittest
from PyDSALib.deque import Deque


class MyTestCase(unittest.TestCase):
    @staticmethod
    def setup():
        deque = Deque()
        insert_list = [4, 65, 12, 11, 191]
        for i in insert_list:
            deque.left_enqueue(i)

        return deque

    def test_left_methods(self):
        deque = self.setup()
        deque.left_enqueue(10)
        self.assertEqual(deque.left_dequeue(), 10)
        self.assertEqual(deque.left_dequeue(), 191)

    def test_right_methods(self):
        deque = self.setup()
        deque.right_enqueue(10)
        self.assertEqual(deque.right_dequeue(), 10)
        self.assertEqual(deque.right_dequeue(), 4)


if __name__ == '__main__':
    unittest.main()
