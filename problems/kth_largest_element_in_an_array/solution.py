class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapify(heap)
        for i in range(len(nums) - k):
            heappop(heap)
        return heap[0]