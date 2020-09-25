#! usr/bin/env python2.7

from PyDSL.heap import MaxHeap
from PyDSL.heap import MinHeap


class MaxPriorityQueue(MaxHeap):

    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        self.insert(item)

    def dequeue(self):
        return self.pop()

    def is_empty(self):
        return self.heap_size == 0

    def peek(self):
        return self.heap_list[1]

    def get_size(self):
        return self.heap_size

    def enqueue_list(self, en_list):
        self.build(en_list)

    def change_val(self, val, new_key):
        self.heap_change_val(val, new_key)

    def __repr__(self):
        return '{}'.format([item for item in self.heap_list if item != 0])


class MinPriorityQueue(MinHeap):

    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        self.insert(item)

    def dequeue(self):
        return self.pop()

    def is_empty(self):
        return self.heap_size == 0

    def peek(self):
        return self.heap_list[1]

    def get_size(self):
        return self.heap_size

    def enqueue_list(self, en_list):
        self.build(en_list)

    def change_val(self, val, new_key):
        self.heap_change_val(val, new_key)

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





