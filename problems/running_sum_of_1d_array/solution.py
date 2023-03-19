class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum: List[int] = list()
        for i in range(len(nums)):
            if (i == 0):
                sum.append(nums[i])
            else:
                sum.append(sum[i-1] + nums[i])
        return sum