class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid[0])):
            col = [grid[j][i] for j in range(len(grid))]
            for k in grid:
                if col == k:
                    count += 1
        return count