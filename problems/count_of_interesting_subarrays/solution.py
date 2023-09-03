class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefixSum = {0:1}
        res = 0
        currSum = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                currSum += 1
            currSum = currSum % modulo
            val = (currSum - k) % modulo
            res += prefixSum.get(val, 0)
            prefixSum[currSum] = prefixSum.get(currSum,0) + 1
        
        return res