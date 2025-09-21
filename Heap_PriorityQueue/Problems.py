# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

def lastStoneWeight(stones):
    maxHeap = []

    for s in stones:
        heapq.heappush(maxHeap, -s)

    while len(maxHeap) > 1:
        stone1 = -heapq.heappop(maxHeap)
        stone2 = -heapq.heappop(maxHeap)

        if stone1 < stone2:
            stone2 -= stone1
            heapq.heappush(maxHeap, -stone2)
        else:
            stone1 -= stone2
            heapq.heappush(maxHeap, -stone1)

    return -maxHeap[0] if maxHeap else 0