
from PyDSL.linked_list import Node
from PyDSL.linked_list import LinkedList


class Queue(LinkedList):

    def __init__(self):
        super().__init__()
        self.tail = None

    def enqueue(self, item):
        item_to_add = Node(item)
        item_to_add.set_next(self.head)

        if not self.tail:
            self.tail = item_to_add
        else:
            self.head.set_prev(item_to_add)

        self.head = item_to_add
        self.size += 1

    def dequeue(self):
        next_last = self.tail.get_prev()
        last = self.tail
        self.tail = next_last
        self.size -= 1

        return last.get_data()

    def peek(self):
        return self.tail.get_data()





