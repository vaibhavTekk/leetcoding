class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        j = 1
        arr = [j]
        n-=1
        while (n > 0):
            j += 1
            if (k - j) not in arr:
                arr += [j]
                n -= 1
        print(arr)
        return sum(arr)