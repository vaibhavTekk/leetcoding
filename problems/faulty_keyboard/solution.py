class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for i in s:
            if i == 'i':
                res = self.reverse(res)
            else:
                res += i
        return res
    
    def reverse(self,s):
        res = ''
        for i in range(len(s)-1,-1,-1):
            res += s[i]
        return res
            