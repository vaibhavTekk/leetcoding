class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        while(i < n and j < n):
            if not nums[j] == val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i 