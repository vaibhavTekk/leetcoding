class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        vals = [-int(i) for i in nums]
        heapify(vals)
        for i in range(k-1):
            heappop(vals)
        return str(-heappop(vals))