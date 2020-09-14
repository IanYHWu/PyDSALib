
from linked_list import Node
from linked_list import LinkedList


class Deque(LinkedList):

    def __init__(self):
        super().__init__()
        self.tail = None

    def left_enqueue(self, item):
        item_to_add = Node(item)
        item_to_add.set_next(self.head)

        if not self.tail:
            self.tail = item_to_add
        else:
            self.head.set_prev(item_to_add)

        self.head = item_to_add
        self.size += 1

    def right_enqueue(self, item):
        item_to_add = Node(item)
        item_to_add.set_prev(self.tail)

        if not self.head:
            self.head = item_to_add
        else:
            self.tail.set_next(item_to_add)

        self.tail = item_to_add
        self.size += 1

    def left_dequeue(self):
        next_head = self.head.get_next()
        head = self.head
        self.head = next_head
        self.size -= 1

        return head.get_data()

    def right_dequeue(self):
        next_last = self.tail.get_prev()
        last = self.tail
        self.tail = next_last
        self.size -= 1

        return last.get_data()




