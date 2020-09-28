from PyDSL.linked_list import Node
from PyDSL.linked_list import LinkedList


class Deque(LinkedList):
    """Node class for deque. Extends LinkedList

        Attributes:
            head: Node object. The head of the deque
            tail: Node object. The tail of the deque
            size: the length of the deque
    """

    def __init__(self):
        """Initialise Deque class"""
        super().__init__()
        self.tail = None

    def left_enqueue(self, item):
        """Add an item to the left of the deque"""
        item_to_add = Node(item)
        item_to_add.set_next(self.head)

        # if the deque is empty, the new item is the tail
        if not self.tail:
            self.tail = item_to_add
        else:
            # connect the old head to the new head
            self.head.set_prev(item_to_add)

        # set the new node as the head
        self.head = item_to_add
        self.size += 1

    def right_enqueue(self, item):
        """Add an item to the right of the deque"""
        item_to_add = Node(item)
        item_to_add.set_prev(self.tail)

        # if the deque is empty, the new item is the head
        if not self.head:
            self.head = item_to_add
        else:
            # connect the old tail to the new tail
            self.tail.set_next(item_to_add)

        self.tail = item_to_add
        self.size += 1

    def left_dequeue(self):
        """Remove an item from the left of the deque and return it"""
        # get the next head and set it as the new head. Save the old head
        next_head = self.head.get_next()
        head = self.head
        self.head = next_head
        self.size -= 1

        # return the data in the old head
        return head.get_data()

    def right_dequeue(self):
        """Remove an item from the right of the deque and return it"""
        # get the next tail and set it as the new tail. Save the oldtail
        next_last = self.tail.get_prev()
        last = self.tail
        self.tail = next_last
        self.size -= 1

        # return the data in the old tail
        return last.get_data()




