class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def helper(arr,curr,currsum,index):
            if len(curr) == k:
                if currsum == n:
                    arr.append(curr)
                return
            if currsum > n:
                return
            
            for i in range(index, 10):
                helper(arr,curr + [i], currsum + i, i+1)
        
        arr = []
        helper(arr,[],0,1)
        return arr