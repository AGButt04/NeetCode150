# This file has all the problems in the Sliding Window
# section of the NeetCode150 with the explanations.

import heapq
import math

class KthLargest:
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)   # O(n) to build heap
        while len(self.minHeap) > k:  # Keep only k largest
            heapq.heappop(self.minHeap)  # O(log n) each

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # O(log k)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)    # O(log k)

        # Time Complexity:
        #   __init__: O(n + (n-k) log n) ≈ O(n) for heapify + O((n-k) log n) trimming
        #   add(): O(log k)
        # Space Complexity: O(k) (heap stores k elements max)
        return self.minHeap[0]             # Kth largest element


def lastStoneWeight(stones):
    maxHeap = []
    for s in stones:
        heapq.heappush(maxHeap, -s)  # Python has min-heap → use negatives
    # O(n log n) to push all

    while len(maxHeap) > 1:
        stone1 = -heapq.heappop(maxHeap)  # Largest stone
        stone2 = -heapq.heappop(maxHeap)  # 2nd largest stone
        if stone1 < stone2:
            heapq.heappush(maxHeap, -(stone2 - stone1))  # Push difference
        elif stone1 > stone2:
            heapq.heappush(maxHeap, -(stone1 - stone2))
        # If equal → both destroyed → nothing pushed

    # Time Complexity: O(n log n) (each heap pop/push is O(log n), up to n operations)
    # Space Complexity: O(n) (heap stores all stones)
    return -maxHeap[0] if maxHeap else 0

def findKthLargest(nums, k):
    minHeap = []
    for n in nums:
        heapq.heappush(minHeap, n)    # O(log k) when size ≤ k
        if len(minHeap) > k:
            heapq.heappop(minHeap)    # Pop smallest if heap too big

    # Time Complexity: O(n log k) (each push/pop is O(log k), done n times)
    # Space Complexity: O(k) (heap of size k)
    return minHeap[0]  # Root is kth largest

def kClosest(points, k):
    maxHeap = []
    closestPoints = []

    for i in range(len(points)):
        x = math.pow(points[i][0], 2)
        y = math.pow(points[i][1], 2)
        distance = math.sqrt(x + y)

        heapq.heappush(maxHeap, (-distance, i))
        if len(maxHeap) > k:
            heapq.heappop(maxHeap)

    while maxHeap:
        _, i = heapq.heappop(maxHeap)
        closestPoints.append(points[i])

    return closestPoints

if __name__ == '__main__':
    points = [[0, 2], [2, 0], [2, 2]]
    k = 2
    print(kClosest(points, k))
