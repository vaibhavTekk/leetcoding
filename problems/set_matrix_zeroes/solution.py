class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    arr.append([i,j])
        for i in arr:
            for j in range(len(matrix)):
                matrix[j][i[1]] = 0
            for k in range(len(matrix[0])):
                matrix[i[0]][k] = 0
