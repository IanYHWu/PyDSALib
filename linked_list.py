"""
Linked list class
"""


class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.previous

    def set_data(self, input_data):
        self.data = input_data

    def set_next(self, input_next):
        self.next = input_next

    def set_prev(self, input_prev):
        self.previous = input_prev


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def remove(self, item):
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
        return self.size

    def search(self, item):
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

    









