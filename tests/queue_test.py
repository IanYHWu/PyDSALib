import unittest
from PyDSALib.queue import Queue


class QueueTest(unittest.TestCase):
    @staticmethod
    def setup():
        q = Queue()
        list_items = [22, 43, 1, 76]
        for item in list_items:
            q.enqueue(item)

        return q

    def test_methods(self):
        q = self.setup()
        q.enqueue(78)
        self.assertEqual(q.get_size(), 5)
        self.assertEqual(q.dequeue(), 22)
        self.assertEqual(q.dequeue(), 43)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 76)
        self.assertEqual(q.dequeue(), 78)


if __name__ == '__main__':
    unittest.main()
