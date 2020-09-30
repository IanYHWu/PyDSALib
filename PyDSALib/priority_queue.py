#! usr/bin/env python2.7

from PyDSALib.heap import MaxHeap
from PyDSALib.heap import MinHeap


class MaxPriorityQueue(MaxHeap):
    """Heap-based max priority queue. The node with maximum key is prioritised.
        Provides queue-like methods for the MaxHeap class. Extends the MaxHeap class

        Attributes:
            heap_list: the list of HeapNodes. The first element is always an empty node that is ignored by operations
            heap_size: the number of elements in the heap. Starts at 0
    """

    def __init__(self):
        """Initialise the MaxPriorityQueue"""
        super().__init__()

    def enqueue(self, item):
        """Insert item into MaxPriorityQueue"""
        self.insert(item)

    def dequeue(self):
        """Remove item from MaxPriorityQueue"""
        return self.pop()

    def is_empty(self):
        """Check if MaxPriorityQueue is empty"""
        return self.heap_size == 0

    def peek(self):
        """Return the first element of the MaxPriorityQueue"""
        return self.heap_list[1]

    def get_size(self):
        """Get the size of the MaxPriorityQueue"""
        return self.heap_size

    def enqueue_list(self, en_list):
        """Converts a list into a MaxPriorityQueue"""
        self.build(en_list)

    def change_key(self, val, new_key):
        """For priority queues containing tuples - change the keys of items with values val"""
        self.heap_change_key(val, new_key)

    def __repr__(self):
        return '{}'.format([item for item in self.heap_list if item != 0])


class MinPriorityQueue(MinHeap):
    """Heap-based min priority queue. The node with minimum key is prioritised.
        Provides queue-like methods for the MinHeap class. Extends the MinHeap class

        Attributes:
            heap_list: the list of HeapNodes. The first element is always an empty node that is ignored by operations
            heap_size: the number of elements in the heap. Starts at 0
    """

    def __init__(self):
        """Initialise the MinPriorityQueue"""
        super().__init__()

    def enqueue(self, item):
        """Insert item into MinPriorityQueue"""
        self.insert(item)

    def dequeue(self):
        """Remove item from MinPriorityQueue"""
        return self.pop()

    def is_empty(self):
        """Check if MinPriorityQueue is empty"""
        return self.heap_size == 0

    def peek(self):
        """Return the first element of the MinPriorityQueue"""
        return self.heap_list[1]

    def get_size(self):
        """Get the size of the MinPriorityQueue"""
        return self.heap_size

    def enqueue_list(self, en_list):
        """Converts a list into a MinPriorityQueue"""
        self.build(en_list)

    def change_key(self, val, new_key):
        """For priority queues containing tuples - change the keys of items with values val"""
        self.heap_change_key(val, new_key)

    def __repr__(self):
        return '{}'.format([item for item in self.heap_list if item != 0])


if __name__ == '__main__':
    pq = MinPriorityQueue()
    new_list = [(9, 'dog'), (5, 'cat'), (6, 'bear'), (2, 'horse'), (3, 'snake'), (4, 'ant'), (8, 'bird')]
    pq.enqueue_list(new_list)
    print(pq.peek())
    print(pq.dequeue())
    print(pq.get_size())
    print(pq.dequeue())
    print(pq.get_size())
    print(pq.dequeue())
    print(pq.dequeue())
    print(pq)





