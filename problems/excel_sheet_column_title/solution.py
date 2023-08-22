class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            res += chr(((columnNumber - 1)%26) + ord('A'))
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]