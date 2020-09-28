
class HeapNode:
    """HeapNode class. Forms the elements of the MaxHeap and MinHeap classes

        Attributes:
            data: the data contained in the HeapNode. Can be a float/int or a tuple, with the zeroth element of the
            tuple acting as the key
    """

    def __init__(self, data):
        """Initialise the HeapNode object"""
        self.data = data

    def get_data(self):
        """Get the data contained in the HeapNode"""
        return self.data

    def set_data(self, item):
        """Set the data contained in the HeapNode"""
        self.data = item

    def __lt__(self, other):
        """Allows for comparison of HeapNodes. With tuple data, compares the zeroth element of the tuples"""
        if type(self.data) is float or type(self.data) is int:
            if self.data < other.data:
                # compare data attribute directly if data is a float/int
                return True
            else:
                return False
        elif type(self.data) is tuple:
            if self.data[0] < other.data[0]:
                # compare zeroth element of data attribute if data is tuple
                return True
            else:
                return False

    def __gt__(self, other):
        """Allows for comparison of HeapNodes. With tuple data, compares the zeroth element of the tuples"""
        if type(self.data) is float or type(self.data) is int:
            if self.data > other.data:
                # compare data attribute directly if data is a float/int
                return True
            else:
                return False
        elif type(self.data) is tuple:
            if self.data[0] > other.data[0]:
                # compare zeroth element of data attribute if data is tuple
                return True
            else:
                return False

    def __eq__(self, other):
        """Allows for comparison of HeapNodes. With tuple data, compares the zeroth element of the tuples"""
        if type(self.data) is float or type(self.data) is int:
            if self.data == other.data:
                # compare data attribute directly if data is a float/int
                return True
            else:
                return False
        elif type(self.data) is tuple:
            if self.data[0] == other.data[0]:
                # compare zeroth element of data attribute if data is tuple
                return True
            else:
                return False

    def __repr__(self):
        return str(self.data)


class MinHeap:
    """Class for a min heap - a heap that prioritises the smallest item

        Attributes:
            heap_list: the list of HeapNodes. The first element is always an empty node that is ignored by operations
            heap_size: the number of elements in the heap. Starts at 0
    """

    def __init__(self):
        """Initialise the MinHeap"""
        self.heap_list = [HeapNode(None)]
        self.heap_size = 0

    def _percolate_up(self, i):
        """Move an item up the list"""
        while i // 2 > 0:
            # swap elements if i//2th element is bigger than ith element
            if self.heap_list[i // 2] > self.heap_list[i]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2  # move up the heap_list

    def insert(self, item):
        """Insert an item into the heap"""
        self.heap_list.append(HeapNode(item))
        self.heap_size += 1
        self._percolate_up(self.heap_size)  # place new item into the correct place within heap_list

    def _percolate_down(self, i):
        """Move an item down the list"""
        while i * 2 < self.heap_size:  # keep going until the last layer of the tree is reached
            # compare the left and right children of the ith node. If the left one is smaller...
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                # if the ith node is bigger than the selected node, swap the node and its smaller child
                if self.heap_list[i] > self.heap_list[i * 2]:
                    self.heap_list[i], self.heap_list[i * 2] = self.heap_list[i * 2], self.heap_list[i]
                i = i * 2 # move to next level
            # compare the left and right children of the ith node. If the right one is smaller...
            else:
                # if the ith node is bigger than the selected node, swap the node and its smaller child
                if self.heap_list[i] > self.heap_list[i * 2 + 1]:
                    self.heap_list[i], self.heap_list[i * 2 + 1] = self.heap_list[i * 2 + 1], self.heap_list[i]
                i = i * 2 + 1 # move to next level

    def pop(self):
        """Remove and return the HeapNode of highest priority"""
        if self.heap_size > 1:
            # return the first item in the heap_list, replace with the last item and percolate that down to its
            # correct position
            last_item = self.heap_list.pop()
            min_item = self.heap_list[1]
            self.heap_list[1] = last_item
            self.heap_size -= 1
            self._percolate_down(1)
            return min_item
        else:
            # if the heap_list has only one item, return said item
            min_item = self.heap_list.pop()
            self.heap_size -= 1
            return min_item

    def delete_item(self, item_index):
        """Delete a HeapNode in a specific position (index) within heap_list"""
        # locate target node and replace with last node in the heap_list
        target = self.heap_list[item_index]
        last_item = self.heap_list.pop()
        if item_index == self.heap_size:
            self.heap_size -= 1
        else:
            self.heap_list[item_index] = last_item
            self.heap_size -= 1
            self._percolate_down(item_index)  # percolate down to place replacement node in the correct place
        return target

    def build(self, new_list):
        """Construct a MaxHeap given a list of numbers or tuples"""
        for i in new_list:
            self.insert(i)

    def heap_change_key(self, val, new_key):
        """For heaps containing HeapNodes of tuples - change the keys of items with values val"""
        for index, item in enumerate(self.heap_list):
            if index > 0:
                # delete the node with matching val
                if item.get_data()[1] == val:
                    self.delete_item(index)
        # insert a new node object with the new key and same val
        self.insert((new_key, val))

    def __repr__(self):
        return str([node for node in self.heap_list if node.get_data()])

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
    """Class for a max heap - a heap that prioritises the biggest item

        Attributes:
            heap_list: the list of HeapNodes. The first element is always an empty node that is ignored by operations
            heap_size: the number of elements in the heap. Starts at 0
    """

    def __init__(self):
        """Initialise the MaxHeap"""
        self.heap_list = [HeapNode(None)]
        self.heap_size = 0

    def _percolate_up(self, i):
        """Move an item up the list"""
        while i // 2 > 0:
            # swap elements if i//2th element is smaller than ith element
            if self.heap_list[i // 2] < self.heap_list[i]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i = i // 2  # move up the heap_list

    def insert(self, item):
        """Insert an item into the heap"""
        self.heap_list.append(HeapNode(item))
        self.heap_size += 1
        self._percolate_up(self.heap_size)  # place new item into the correct place within heap_list

    def _percolate_down(self, i):
        """Move an item down the list"""
        while i * 2 < self.heap_size:
            # keep going until the last layer of the tree is reached
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                # compare the left and right children of the ith node. If the left one is bigger...
                if self.heap_list[i] < self.heap_list[i * 2]:
                    # if the ith node is smaller than the selected node, swap the node and its bigger child
                    self.heap_list[i], self.heap_list[i * 2] = self.heap_list[i * 2], self.heap_list[i]
                i = i * 2  # move to next level
            else:
                # compare the left and right children of the ith node. If the right one is bigger...
                if self.heap_list[i] < self.heap_list[i * 2 + 1]:
                    # if the ith node is smaller than the selected node, swap the node and its bigger child
                    self.heap_list[i], self.heap_list[i * 2 + 1] = self.heap_list[i * 2 + 1], self.heap_list[i]
                i = i * 2 + 1  # move to next level

    def pop(self):
        """Remove and return the HeapNode of highest priority"""
        if self.heap_size > 1:
            # return the first item in the heap_list, replace with the last item and percolate that down to its
            # correct position
            last_item = self.heap_list.pop()
            min_item = self.heap_list[1]
            self.heap_list[1] = last_item
            self.heap_size -= 1
            self._percolate_down(1)
            return min_item
        else:
            # if the heap_list has only one item, return said item
            min_item = self.heap_list.pop()
            self.heap_size -= 1
            return min_item

    def delete_item(self, item_index):
        """Delete a HeapNode in a specific position (index) within heap_list"""
        # locate target node and replace with last node in the heap_list
        target = self.heap_list[item_index]
        last_item = self.heap_list.pop()
        if item_index == self.heap_size:
            self.heap_size -= 1
        else:
            self.heap_list[item_index] = last_item
            self.heap_size -= 1
            self._percolate_down(item_index)  # percolate down to place replacement node in the correct place
        return target

    def build(self, new_list):
        """Construct a MaxHeap given a list of numbers or tuples"""
        for i in new_list:
            self.insert(i)

    def heap_change_key(self, val, new_key):
        """For heaps containing HeapNodes of tuples - change the keys of items with values val"""
        for index, item in enumerate(self.heap_list):
            if index > 0:
                # delete the node with matching val
                if item.get_data()[1] == val:
                    self.delete_item(index)
        # insert a new node object with the new key and same val
        self.insert((new_key, val))

    def __repr__(self):
        return str([node for node in self.heap_list if node.get_data()])

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
    bin_heap.insert((1, 'Shark'))
    bin_heap.delete_item(3)
    print(bin_heap.heap_list)
    bin_heap.heap_change_key('cat', 10)
    print(bin_heap)
    print('lion' in bin_heap)
