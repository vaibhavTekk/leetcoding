class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def helper(arr,curr,currSum,index):
            if currSum > target:
                return
            if currSum == target:
                arr.append(curr)
                return 
            for i in range(index,len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                val = candidates[i]
                helper(arr,curr + [val],currSum + val,i+1)
        arr = []
        helper(arr,[],0,0)
        return arr