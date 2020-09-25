
class HeapNode:

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, item):
        self.data = item

    def __lt__(self, other):
        if type(self.data) is float or type(self.data) is int:
            if self.data < other.data:
                return True
            else:
                return False
        elif type(self.data) is tuple:
            if self.data[0] < other.data[0]:
                return True
            else:
                return False

    def __gt__(self, other):
        if type(self.data) is float or type(self.data) is int:
            if self.data > other.data:
                return True
            else:
                return False
        elif type(self.data) is tuple:
            if self.data[0] > other.data[0]:
                return True
            else:
                return False

    def __eq__(self, other):
        if type(self.data) is float or type(self.data) is int:
            if self.data == other.data:
                return True
            else:
                return False
        elif type(self.data) is tuple:
            if self.data[0] == other.data[0]:
                return True
            else:
                return False

    def __repr__(self):
        return str(self.data)


class MinHeap:

    # MinHeap - the children are always bigger than the parent

    def __init__(self):
        self.heap_list = [HeapNode(None)]
        self.heap_size = 0

    def perlocate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i // 2] > self.heap_list[i]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, item):
        self.heap_list.append(HeapNode(item))
        self.heap_size += 1
        self.perlocate_up(self.heap_size)

    def perlocate_down(self, i):
        while i * 2 < self.heap_size:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                if self.heap_list[i] > self.heap_list[i * 2]:
                    self.heap_list[i], self.heap_list[i * 2] = self.heap_list[i * 2], self.heap_list[i]
                i = i * 2
            else:
                if self.heap_list[i] > self.heap_list[i * 2 + 1]:
                    self.heap_list[i], self.heap_list[i * 2 + 1] = self.heap_list[i * 2 + 1], self.heap_list[i]
                i = i * 2 + 1

    def pop(self):
        if self.heap_size > 1:
            last_item = self.heap_list.pop()
            min_item = self.heap_list[1]
            self.heap_list[1] = last_item
            self.heap_size -= 1
            self.perlocate_down(1)
            return min_item
        else:
            min_item = self.heap_list.pop()
            self.heap_size -= 1
            return min_item

    def delete_item(self, item_index):
        target = self.heap_list[item_index]
        last_item = self.heap_list.pop()
        if item_index == self.heap_size:
            self.heap_size -= 1
        else:
            self.heap_list[item_index] = last_item
            self.heap_size -= 1
            self.perlocate_down(item_index)
        return target

    def build(self, new_list):
        for i in new_list:
            self.insert(i)

    def heap_change_val(self, val, new_key):
        for index, item in enumerate(self.heap_list):
            if index > 0:
                if item.get_data()[1] == val:
                    self.delete_item(index)
        self.insert((new_key, val))

    def __repr__(self):
        return str([node for node in self.heap_list])

    def __contains__(self, val):
        contained = False
        for node in self.heap_list:
            if type(node.get_data()) is tuple:
                if node.get_data()[1] == val:
                    contained = True
                    break
            else:
                if node.get_data() == val:
                    contained = True
                    break
        return contained

    def __iter__(self):
        return iter(node.get_data() for node in self.heap_list)


class MaxHeap:
    """Class for a max heap - a heap with the biggest item on top

        Attributes:
            heap_list: the list of items (numbers) inside the heap
            heap_size: the number of items inside the heap
    """

    def __init__(self):
        """Initialises the MaxHeap"""
        self.heap_list = [HeapNode(None)]
        self.heap_size = 0

    def perlocate_up(self, i):
        """Moves an item up the list"""
        while i // 2 > 0:
            if self.heap_list[i // 2] < self.heap_list[i]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, item):
        """Inserts an item in the correct place in the list"""
        self.heap_list.append(HeapNode(item))
        self.heap_size += 1
        self.perlocate_up(self.heap_size)

    def perlocate_down(self, i):
        """Moves an item down the list"""
        while i * 2 < self.heap_size:
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                if self.heap_list[i] < self.heap_list[i * 2]:
                    self.heap_list[i], self.heap_list[i * 2] = self.heap_list[i * 2], self.heap_list[i]
                i = i * 2
            else:
                if self.heap_list[i] < self.heap_list[i * 2 + 1]:
                    self.heap_list[i], self.heap_list[i * 2 + 1] = self.heap_list[i * 2 + 1], self.heap_list[i]
                i = i * 2 + 1

    def pop(self):
        if self.heap_size > 1:
            last_item = self.heap_list.pop()
            min_item = self.heap_list[1]
            self.heap_list[1] = last_item
            self.heap_size -= 1
            self.perlocate_down(1)
            return min_item
        else:
            min_item = self.heap_list.pop()
            self.heap_size -= 1
            return min_item

    def delete_item(self, item_index):
        target = self.heap_list[item_index]
        last_item = self.heap_list.pop()
        if item_index == self.heap_size:
            self.heap_size -= 1
        else:
            self.heap_list[item_index] = last_item
            self.heap_size -= 1
            self.perlocate_down(item_index)
        return target

    def build(self, new_list):
        """Constructs a MaxHeap given a list of numbers"""
        for i in new_list:
            self.insert(i)

    def heap_change_val(self, val, new_key):
        for index, item in enumerate(self.heap_list):
            if index > 0:
                if item.get_data()[1] == val:
                    self.delete_item(index)
        self.insert((new_key, val))

    def __repr__(self):
        return str([node for node in self.heap_list])

    def __contains__(self, val):
        contained = False
        for node in self.heap_list:
            if type(node.get_data()) is tuple:
                if node.get_data()[1] == val:
                    contained = True
                    break
            else:
                if node.get_data() == val:
                    contained = True
                    break
        return contained

    def __iter__(self):
        return iter(node.get_data() for node in self.heap_list)


if __name__ == '__main__':
    bin_heap = MaxHeap()
    # new_list = [HeapNode((9, 'dog')), HeapNode((5, 'cat')), HeapNode((6, 'bear')), HeapNode((2, 'horse')),
    #             HeapNode((3, 'snake')), HeapNode((4, 'ant')), HeapNode((8, 'bird'))]
    new_list = [(9, 'dog'), (5, 'cat'), (6, 'bear'), (2, 'horse'), (3, 'snake'), (4, 'ant'), (8, 'bird')]
    bin_heap.build(new_list)
    print(bin_heap)
    print(bin_heap)
    print(bin_heap.pop())
    print(bin_heap.pop())
    print(bin_heap.heap_list)
    bin_heap.insert((1, 'Shark'))
    bin_heap.delete_item(3)
    print(bin_heap.heap_list)
    bin_heap.heap_change_val('cat', 10)
    print(bin_heap)
    print('lion' in bin_heap)
