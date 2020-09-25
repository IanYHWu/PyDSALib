
class HeapNode:

    def __init__(self, data):
        self.data = data

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
        else:
            raise TypeError

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
            else:
                raise TypeError


class MinHeap:

    # MinHeap - the children are always bigger than the parent

    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def perlocate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i // 2] > self.heap_list[i]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, item):
        self.heap_list.append(item)
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
        last_item = self.heap_list.pop()
        min_item = self.heap_list[1]
        self.heap_list[1] = last_item
        self.heap_size -= 1
        self.perlocate_down(1)
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
        i = len(new_list) // 2
        self.heap_size = len(new_list)
        self.heap_list = self.heap_list + new_list
        while i > 0:
            self.perlocate_down(i)
            i -= 1

class MaxHeap:
    """Class for a max heap - a heap with the biggest item on top

        Attributes:
            heap_list: the list of items (numbers) inside the heap
            heap_size: the number of items inside the heap
    """

    def __init__(self):
        """Initialises the MaxHeap"""
        self.heap_list = [0]
        self.heap_size = 0

    def perlocate_up(self, i):
        """Moves an item up the list"""
        while i // 2 > 0:
            if self.heap_list[i // 2] < self.heap_list[i]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2

    def insert(self, item):
        """Inserts an item in the correct place in the list"""
        self.heap_list.append(item)
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
        """Removes and returns the item at the top of the list (the maximum number)"""
        last_item = self.heap_list.pop()
        max_item = self.heap_list[1]
        self.heap_list[1] = last_item
        self.heap_size -= 1
        self.perlocate_down(1)
        return max_item

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
        i = len(new_list) // 2
        self.heap_size = len(new_list)
        self.heap_list = self.heap_list + new_list
        while i > 0:
            self.perlocate_down(i)
            i -= 1


if __name__ == '__main__':
    bin_heap = MinHeap()
    new_list = [9, 5, 6, 2, 3, 4, 8]
    bin_heap.build(new_list)
    print(bin_heap.heap_list)
    bin_heap.insert(1)
    print(bin_heap.heap_list)
    print(bin_heap.pop())
    print(bin_heap.pop())
    print(bin_heap.heap_list)

    bin_heap.delete_item(3)
    print(bin_heap.heap_list)
