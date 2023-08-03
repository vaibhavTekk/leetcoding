class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        digits = list(digits)
        vals = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        arr = []
        def backtrack(k,curr):
            if len(curr) == n:
                arr.append(curr)
                return
            for i in vals[int(digits[k])]:
                backtrack(k+1,curr + i)
        
        if digits:
            backtrack(0,"")
            return arr
        return []