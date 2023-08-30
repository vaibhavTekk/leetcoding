class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i,j,ind):
            if ind == len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] != word[ind]:
                return False

            temp = board[i][j]
            board[i][j] = '#'
            res = backtrack(i+1,j,ind+1) or backtrack(i,j+1,ind+1) or backtrack(i-1,j,ind+1) or backtrack(i,j-1,ind+1)            
            board[i][j] = temp
            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
