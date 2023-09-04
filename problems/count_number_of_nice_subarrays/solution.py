class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        res = 0
        currSum = 0
        for i in nums:
            if i % 2 != 0:
                currSum += 1
            
            val = currSum - k
            res += prefixSum.get(val,0)

            prefixSum[currSum] = 1 + prefixSum.get(currSum,0)
        return res