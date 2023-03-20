class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n = len(t)
        m = len(s)
        if m == 0:
            return True
        while(j<n and i<m):
            if s[i] == t[j]:
                i += 1
            j += 1
        if (i == len(s)):
            return True
        else:
            return False