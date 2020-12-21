import heapq as heap
class MedianFinder:

    def __init__(self):
        self.minheap= []
        self.maxheap = []
        
        

    def addNum(self, num: int) -> None:
        if len(self.maxheap) == 0 or num < -self.maxheap[0]:
            heap.heappush(self.maxheap,-num)
        else:
            heap.heappush(self.minheap,num)
        if len(self.maxheap)> len(self.minheap)+1:
            popped = heap.heappop(self.maxheap)
            heap.heappush(self.minheap,-popped)
        elif len(self.minheap) > len(self.maxheap)+1:
            popped = heap.heappop(self.minheap)
            heap.heappush(self.maxheap,-popped)
        

    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0])/2
        elif len(self.minheap)> len(self.maxheap):
            return self.minheap[0]
        else:
            return -self.maxheap[0]
        
O(logn) -> Time
O(n) -> Space

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
