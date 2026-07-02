class minHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
# Time O(n) | O(1) Space

    def buildHeap(self, array):
        lastparentIdx = (len(array) - 2) // 2
        for i in reversed(range(lastparentIdx)):
            self.siftDown(i, len(array) - 1, array)
        return array
# O(log(n)) Time | O(1) Space

    def siftDown(self, currentIdx, endIdx, array):
        childoneIdx = (currentIdx * 2) + 1
        while childoneIdx <= endIdx:
            childtwoIdx = (currentIdx *
                           2) + 2 if (currentIdx * 2) + 2 <= endIdx else -1
            if childtwoIdx != -1 and array[childoneIdx] > array[childtwoIdx]:
                indextoswap = childtwoIdx
            else:
                indextoswap = childoneIdx
            if array[indextoswap] < array[currentIdx]:
                self.swap(currentIdx, indextoswap, array)
                currentIdx = indextoswap
                childoneIdx = (currentIdx * 2) + 1
            else:
                break

# O(log(n)) Time | O(1) Space

    def siftUp(self, currentIdx, array):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and array[currentIdx] < array[parentIdx]:
            self.swap(currentIdx, parentIdx, array)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

# O(log(n)) Time | O(1) Space

    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        removedVal = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removedVal


# O(log(n)) Time | O(1) Space

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

object = minHeap([23, 12, 8, 17, 31, 30, 44, 102, 18])
print(object.heap)
print(object.remove())
print(object.insert(9))
print(object.heap)
