class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum = 0
        for i in num2:
            rowsum = 0
            for j in num1:
                rowsum *= 10
                p = int(j)*int(i)
                rowsum += p
            sum *= 10
            sum += rowsum
        return str(sum)