def isCellValid(i,j,val,board):
    #check row
    for k in range(9):
        if k != j and board[i][k] == val:
            print("row",i,k)
            return False
    #check col
    for l in range(9):
        if l != i and board[l][j] == val:
            print("col",l,j)
            return False
    #check 3x3 grid
    for p in range(3):
        for q in range(3):
            a = (i//3)*3 + p
            b = (j//3)*3 + q
            if a != i and b != j and board[a][b] == val:
                return False
    return True
            

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if(isCellValid(i,j,board[i][j],board) == False):
                        print(i,j)
                        return False
        return True