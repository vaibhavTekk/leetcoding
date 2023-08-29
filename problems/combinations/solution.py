class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(arr,curr,index):
            if len(curr) == k:
                arr.append(curr)
                return
            if index > n:
                return
            newcurr = curr + [index]
            helper(arr,newcurr,index+1)
            helper(arr,curr,index+1)

        arr = []
        helper(arr,[],1)
        return arr