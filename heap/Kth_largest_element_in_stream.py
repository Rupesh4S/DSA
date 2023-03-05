"""
Kth largest Element in a Stream
"""
import heapq


class Solution:
    """
    Returns Kth largest Element in a Stream
    """

    def __init__(self, k: int, nums: list):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Function to add element in stream
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
