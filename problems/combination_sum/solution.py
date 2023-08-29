class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(arr,curr,currSum,index):
            if currSum > target:
                return
            if currSum == target:
                arr.append(curr)
                return 
            for i in range(index,len(candidates)):
                val = candidates[i]
                helper(arr,curr + [val],currSum + val,i)
        arr = []
        helper(arr,[],0,0)
        return arr