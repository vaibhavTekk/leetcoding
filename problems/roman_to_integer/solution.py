class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'':0}
        prev = ''
        result = 0
        for i in range(len(s)-1,-1,-1):
            curr = s[i]
            if romans[curr] < romans[prev]:
                result -= romans[curr]
            else:
                result += romans[curr]
            prev = curr
        return result
            