class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        res = 0
        currsum = 0
        for i in range(len(nums)):
            currsum += nums[i]
            if currsum % k in prefixSums:
                res += prefixSums[currsum % k]
            
            if currsum % k in prefixSums:
                prefixSums[currsum % k] += 1
            else:
                prefixSums[currsum % k] = 1

        return res

        