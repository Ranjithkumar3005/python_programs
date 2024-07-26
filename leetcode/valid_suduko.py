class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col={}
        row={}
        h1={}
        h2={}
        h3={}
        for i in range(0,9):
            for j in range(9-1,-1,-1):
                if board[j][i] in col:
                    return False
                elif board[j][i] !=".":
                    col[board[j][i]]=0 
            col={}
        for i in range(0,9):
            for j in range(0,9):
                if j<3:
                    if board[i][j] in h1:
                        return False
                    elif board[i][j] !=".":
                       h1[board[i][j]]=0
                elif j<6:
                    if board[i][j] in h2:
                        return False
                    elif board[i][j] !=".":
                       h2[board[i][j]]=0
                else:
                    if board[i][j] in h3:
                        return False
                    elif board[i][j] !=".":
                       h3[board[i][j]]=0
                if board[i][j] in row:
                    return False
                elif board[i][j] !=".":
                    row[board[i][j]]=0 
            if i==2:
                h1={}
                h2={}
                h3={}
            if i==5:
                h1={}
                h2={}
                h3={}
            
            row={}
        return True

s=Solution()
print(s.isValidSudoku( board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))