class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxsum = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if self.maxdigit(nums[i]) == self.maxdigit(nums[j]) and i != j:
                    currsum = nums[i] + nums[j]
                    if currsum > maxsum:
                        maxsum = currsum
        return maxsum
    
    def maxdigit(self,num):
        numlist = [int(i) for i in str(num)]
        return max(numlist)