import heapq
from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Convert strings to integers for numerical comparison
        nums = [int(n) for n in nums]

        # Use a min-heap to keep track of the k largest elements.
        # This is more efficient than a full sort.
        heap = []

        # Iterate through the numbers
        for num in nums:
            # If the heap isn't full yet, add the number
            if len(heap) < k:
                heapq.heappush(heap, num)
            # If the heap is full and the current number is larger than
            # the smallest element in the heap (the root),
            # pop the smallest and push the new number.
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # The root of the min-heap is the k-th largest element.
        return str(heap[0])