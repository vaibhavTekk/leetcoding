class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict(Counter(nums))
        maxc = -1
        e = -1
        for i in d:
            if d[i] > maxc:
                maxc = d[i]
                e = i
        if (maxc > n/2):
            return e