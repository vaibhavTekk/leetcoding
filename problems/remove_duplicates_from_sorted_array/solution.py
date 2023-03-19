class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)-1
        k = 0
        while(j <= n):
            if(nums[i] == nums[j]):
                j += 1
            else:
                k += 1
                nums[k] = nums[j]
                i = j
                j += 1
        return k+1
            