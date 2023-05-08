def isAnagram(s1 : str, s2:str) -> bool:
    return Counter(s1) == Counter(s2)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict(list())
        for i in range(len(strs)):
            sortedword = str(sorted(strs[i]))
            if sortedword not in d:
                d[sortedword] = [strs[i]]
            else:
                d[sortedword].append(strs[i])

        return d.values()
