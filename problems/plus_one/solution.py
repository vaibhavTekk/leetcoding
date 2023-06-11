class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        i = len(digits) - 1
        while remainder != 0:
            if i > 0:
                sum = digits[i] + remainder
                if sum == 10:
                    digits[i] = 0
                    remainder = 1
                else:
                    digits[i] = sum
                    remainder = 0
                i -= 1
            else:
                sum = digits[i] + remainder
                if sum == 10:
                    digits[i] = 0
                    digits.insert(0,1)
                    remainder = 0
                else:
                    digits[i] = sum
                    remainder = 0
        return digits

            