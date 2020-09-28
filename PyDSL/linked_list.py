"""
Linked list class
"""


class Node:
    """Node class for linked list

        Attributes:
            data: the data contained inside the node
            next: Node object. The next node in the linked list
            previous: Node object. The previous node in the linked list
    """

    def __init__(self, init_data):
        """Initialise the TreeNode object

            Arguments:
                init_data: the data of the node
        """
        self.data = init_data
        self.next = None
        self.previous = None

    def get_data(self):
        """Get data of node"""
        return self.data

    def get_next(self):
        """Get the next node"""
        return self.next

    def get_prev(self):
        """Get the previous node"""
        return self.previous

    def set_data(self, input_data):
        """Set data for the node"""
        self.data = input_data

    def set_next(self, input_next):
        """Set the next node"""
        self.next = input_next

    def set_prev(self, input_prev):
        """Set the previous node"""
        self.previous = input_prev


class LinkedList:
    """Node class for linked list

        Attributes:
            head: Node object. The head of the linked list
            size: the length of the linked list
    """

    def __init__(self):
        """Initialise the TreeNode object"""
        self.head = None
        self.size = 0

    def is_empty(self):
        """Check if the linked list is empty"""
        if self.size == 0:
            return True
        else:
            return False

    def remove(self, item):
        """Remove a node with matching data"""
        current = self.head
        previous = None
        found = False

        while not current and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
             
        if found and not previous:
            self.head = current.get_next()
        elif found and previous:
            previous.set_next(current.get_next())
        else:
            raise KeyError('Item not in linked list')

    def get_size(self):
        """Get the size of the LinkedList"""
        return self.size

    def search(self, item):
        """Search for a node with matching data. Return True if found, False if not"""
        current = self.head
        found = False

        while not current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        if not current and not found:
            return False
        else:
            return True

    def insert(self, item, index):
        """Insert a node at an index"""
        item_to_add = Node(item)
        current = self.head
        previous = None
        count = 0

        while count < index and current:
            previous = current
            current = current.get_next()
            count += 1

        if previous:
            if current:
                item_to_add.set_next(current)
                previous.set_next(item_to_add)
            else:
                print('Cannot insert - index out of range')
        else:
            item_to_add.set_next(current)
            self.head = item_to_add

    









