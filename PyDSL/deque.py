
from PyDSL.linked_list import Node
from PyDSL.linked_list import LinkedList


class Deque(LinkedList):
    """Node class for deque. Inherits from LinkedList

        Attributes:
            head: Node object. The head of the deque
            tail: Node object. The tail of the deque
            size: the length of the deque
    """

    def __init__(self):
        super().__init__()
        self.tail = None

    def left_enqueue(self, item):
        """Adds an item to the left of the deque"""
        item_to_add = Node(item)
        item_to_add.set_next(self.head)

        if not self.tail:
            self.tail = item_to_add
        else:
            self.head.set_prev(item_to_add)

        self.head = item_to_add
        self.size += 1

    def right_enqueue(self, item):
        """Adds an item to the right of the deque"""
        item_to_add = Node(item)
        item_to_add.set_prev(self.tail)

        if not self.head:
            self.head = item_to_add
        else:
            self.tail.set_next(item_to_add)

        self.tail = item_to_add
        self.size += 1

    def left_dequeue(self):
        """Removes an item from the left of the deque and returns it"""
        next_head = self.head.get_next()
        head = self.head
        self.head = next_head
        self.size -= 1

        return head.get_data()

    def right_dequeue(self):
        """Removes an item from the right of the deque and returns it"""
        next_last = self.tail.get_prev()
        last = self.tail
        self.tail = next_last
        self.size -= 1

        return last.get_data()




