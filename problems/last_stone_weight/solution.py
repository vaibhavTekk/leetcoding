class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [(-1)*i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            y = (-1)*(heappop(stones))
            x = (-1)*(heappop(stones))
            if x != y:
                new = y - x
                heappush(stones,(-1)*new)
        if stones:
            return (-1)*stones[0]
        else:
            return 0