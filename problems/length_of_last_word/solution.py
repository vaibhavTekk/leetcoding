class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = -1
        for i in range(n-1,-1,-1):
            if count == -1 and s[i] != " ":
                count  = 0
            if (count >= 0):
                if s[i] == " ":
                    return count
                count += 1
        return count