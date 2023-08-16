class Solution:
    def defangIPaddr(self, address: str) -> str:
        newstr = ''
        for i in address:
            if i == '.':
                newstr += '[.]'
            else:
                newstr += i

        return newstr