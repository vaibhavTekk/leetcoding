import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(Counter(nums))
        arr = []
        keys = list(d.keys())
        values = list(d.values())
        valueindex = np.argsort(values)[::-1]
        d2 = {keys[i] : values[i] for i in valueindex}
        for i in d2:
            print(i)
            if k > 0:
                arr += [i]
                k -= 1
        print(d2)
        return arr
