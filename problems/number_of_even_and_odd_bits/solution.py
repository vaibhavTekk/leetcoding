class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        count = 1
        while(n > 0):
            bit = n%2
            n = n//2
            if (count == 1):
                odd += bit
                count = 0
            else:
                even += bit
                count  = 1
        return[odd,even]
                