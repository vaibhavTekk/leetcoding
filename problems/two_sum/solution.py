class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in dic:
                return [i,dic[target - nums[i]]]
            dic[nums[i]] = i            
            
            