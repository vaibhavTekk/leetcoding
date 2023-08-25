class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = nums1
        heapify(heap)
        for i in nums2:
            heappush(heap,i)

        total = len(heap)
        if total % 2 == 0:
            for i in range(total // 2 - 1):
                heappop(heap)
            a = heappop(heap)
            b = heappop(heap)
            return (a+b)/2
        else:
            for i in range(total // 2):
                heappop(heap)
            return heappop(heap)