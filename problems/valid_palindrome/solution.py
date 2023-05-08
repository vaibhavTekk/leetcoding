class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub(r"[^a-z0-9]","",s)
        i = 0
        j = len(s) - 1
        while (i <= j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

        """
        :type s: str
        :rtype: bool
        """