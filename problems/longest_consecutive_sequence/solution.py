class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        j = 1
        nums = [*set(nums)]
        nums.sort()
        print(nums)
        arr = []
        while (j < len(nums)):
            arr += [nums[j]-nums[i]]
            i += 1
            j += 1
        print(arr)
        streak = 0
        maxstreak = 0 
        if len(nums) == 1:
            return 1
        for i in range(len(arr)):
            if arr[i] == 1:
                streak += 1
            else:
                streak += 1
                if streak > maxstreak:
                    maxstreak = streak
                streak = 0
            if i == len(arr) - 1:
                if streak > 0:
                    streak += 1
                    if streak > maxstreak:
                        maxstreak = streak
                    streak = 0
        return maxstreak
                