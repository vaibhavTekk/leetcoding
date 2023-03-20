class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        dict = {"]":"[","}":"{",")":"("}
        for i in s:
            if i in ["[","{","("]:
                stack.append(i)
            elif i in ["]","}",")"]:
                if stack != []:
                    if dict[i] != stack.pop():
                        return False
                else:
                    return False
        if stack == []:
            return True
        else:
            return False