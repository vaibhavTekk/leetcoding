class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix)
        while top < bottom:
            midrow = (top + bottom) // 2
            if (target > matrix[midrow][-1]):
                top = midrow + 1
            elif (target < matrix[midrow][0]):
                bottom = midrow
            else:
                midrow = (top + bottom) // 2
                break
        left = 0
        right = len(matrix[0])
        # print(midrow)
        while left < right:
            midcol = (left + right) // 2
            if (matrix[midrow][midcol] > target):
                right = midcol
            elif (matrix[midrow][midcol] < target):
                left = midcol + 1
            else:
                return True
                break      

        return False  