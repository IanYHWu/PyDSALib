
from linked_list import Node
from linked_list import LinkedList


class Stack(LinkedList):

    def __init__(self):
        super().__init__()

    def enqueue(self, item):
        item_to_add = Node(item)
        item_to_add.set_next(self.head)
        self.head = item_to_add
        self.size += 1

    def dequeue(self):
        first_item = self.head
        next_item = self.head.get_next()
        self.head = next_item
        self.size -= 1

        return first_item.get_data()


