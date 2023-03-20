class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = list()
        l1dup = dict()
        count1 = 0
        l2 = list()
        l2dup = dict()
        count2 = 0
        for i in range(len(s)):
            if s[i] not in l1dup:
                l1dup[s[i]] = count1
                count1 += 1
            l1.append(l1dup[s[i]])

            if t[i] not in l2dup:
                l2dup[t[i]] = count2
                count2 += 1
            l2.append(l2dup[t[i]])

        if l1 == l2:
            return True
        else:
            return False