class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        m = 0
        while (m <= r):
            if nums[m] == 0:
                swap(nums,l,m)
                l+=1
                m+=1
            elif nums[m] == 2:
                swap(nums,r,m)
                r-=1
            else:
                m+=1

def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
