class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        currsum = 0
        res = 0
        for i in range(len(nums)):
            currsum += nums[i] 
            val = currsum - k
            if val in prefixSums:
                res += prefixSums[val]
            if currsum in prefixSums:
                prefixSums[currsum] += 1
            else:
                prefixSums[currsum] = 1
        return res