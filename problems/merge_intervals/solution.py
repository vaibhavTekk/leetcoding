class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda c: c[0])
        merged = [intervals.pop(0)]
        while len(intervals) > 0:
            curr = merged.pop()
            inter = intervals.pop(0)
            if curr[1] >= inter[0] and curr[0] <= inter[1]:
                curr[1] = max(inter[1],curr[1])
                curr[0] = min(inter[0],curr[0])
                merged.append(curr)
            else:
                merged.append(curr)
                merged.append(inter)
        return merged