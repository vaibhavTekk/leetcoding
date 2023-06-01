class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count =[]
        c=0
        for i in nums:
            c = c ^ i
        return c

