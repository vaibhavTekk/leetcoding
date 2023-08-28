class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def dfs(curr,i):
            if i >= len(nums):
                arr.append(curr)
                return
            dfs(curr + [nums[i]], i+1)
            dfs(curr, i+1)        
        dfs([],0)

        return arr

