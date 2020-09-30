from PyDSALib.linked_list import Node
from PyDSALib.linked_list import LinkedList


class Stack(LinkedList):
    """Stack class (last-in first-out). Extends LinkedList

        Attributes:
            head: Node object. The head of the linked list
            size: the length of the linked list
    """

    def __init__(self):
        """Initialise the stack object"""
        super().__init__()

    def push(self, item):
        """Add item to the stack"""
        item_to_add = Node(item)
        item_to_add.set_next(self.head)  # connect new node to old head
        self.head = item_to_add  # set new node as new head
        self.size += 1

    def pop(self):
        """Remove and return item"""
        first_item = self.head
        next_item = self.head.get_next()  # set new head
        self.head = next_item
        self.size -= 1

        # return the original head
        return first_item.get_data()

    def peek(self):
        """Return the next item from the stack"""
        return self.head.get_data()


