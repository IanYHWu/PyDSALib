from PyDSL.linked_list import Node
from PyDSL.linked_list import LinkedList


class Queue(LinkedList):
    """Queue class (first-in first-out). Extends LinkedList

        Attributes:
            head: Node object. The head of the linked list
            size: the length of the linked list
            tail: Node object. The tail of the linked list
    """

    def __init__(self):
        """Initialise the queue"""
        super().__init__()
        self.tail = None

    def enqueue(self, item):
        """Insert item into the queue"""
        item_to_add = Node(item)
        item_to_add.set_next(self.head)

        # if the queue is empty, the new item is the tail
        if not self.tail:
            self.tail = item_to_add
        else:
            # connect the old head to the new head
            self.head.set_prev(item_to_add)

        self.head = item_to_add
        self.size += 1

    def dequeue(self):
        """Remove and return item from the queue"""
        # get the next head and set it as the new head. Save the old head
        next_last = self.tail.get_prev()
        last = self.tail
        self.tail = next_last
        self.size -= 1

        return last.get_data()

    def peek(self):
        """Return the next item from the queue"""
        return self.tail.get_data()





