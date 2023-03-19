class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x % 10 == 0 and x != 0):
            return False
        if (x >= 0):
            rev = 0
            while (x > rev):
                rev = rev*10 + x%10
                x = x//10
            if rev == x:
                return True
            elif rev // 10 == x:
                return True
        return False