class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low,high+1):
            numstr = str(num)
            if len(numstr) % 2 == 0:
                i = len(numstr)//2
                leftsum = 0
                for k in numstr[:i]:
                    leftsum += int(k)
                rightsum = 0
                for j in numstr[i:]:
                    rightsum += int(j)
                if leftsum == rightsum:
                    count += 1
        return count