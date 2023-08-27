class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        seen = set()
        k = 1
        while len(seen) < n:
            if target - k not in seen:
                seen.add(k)
            k += 1
        return sum(seen)