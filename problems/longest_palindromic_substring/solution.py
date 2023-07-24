class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        maxlen = 0
        n = len(s)
        for k in range(len(s)):
            low = k - 1
            high = k
            while(low >= 0 and high < n and low <= high and s[low] == s[high]):
                if (high - low + 1) > maxlen:
                    start = low
                    end = high
                    maxlen = high - low + 1
                low -=1
                high += 1
            low = k - 1
            high = k + 1
            while(low >= 0 and high < n and low <= high and s[low] == s[high]):
                if (high - low + 1) > maxlen:
                    start = low
                    end = high
                    maxlen = high - low + 1
                low -=1
                high += 1

        return s[start:end+1]
