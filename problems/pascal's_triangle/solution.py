class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1,1])
            else:
                new = [1]
                for j in range(len(result[i-1])-1):
                    new.append(result[i-1][j] + result[i-1][j+1])
                new.append(1)
                result.append(new)
        return result