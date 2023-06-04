class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        while(i <= len(s2)-len(s1)):
            # print(i)
            currentwindow = list(s2[i:i+len(s1)])
            currentwindow.sort()
            s1list = list(s1)
            s1list.sort()
            # print(currentwindow,s1list)
            if currentwindow == s1list:
                return True
            else:
                i += 1
        return False