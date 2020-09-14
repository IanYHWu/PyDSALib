
class MinHeap:

    # minheap - the children are always bigger than the parent

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

    def build(self, new_list):
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
