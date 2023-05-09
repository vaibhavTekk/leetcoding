class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        arr = []
        while (top < bottom and left < right):
            for j in range(left,right):
                arr.append(matrix[top][j])
            top += 1
            for j in range(top,bottom):
                arr.append(matrix[j][right-1])
            right -= 1

            if (not (left < right and top < bottom)):
                break

            for k in range(right-1,left-1,-1):
                arr.append(matrix[bottom-1][k])
            bottom -= 1
            for l in range(bottom-1,top - 1,-1):
                arr.append(matrix[l][left])
            left += 1
        return arr