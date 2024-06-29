class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dum=[[0 for _ in range(0,9)]for _ in range(0,9)]
        hr={}
        hc={}
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] not in hr or board[i][j]==".":
                    hr[board[i][j]]=1
                else:
                    print(board[i][j])
                    return False
                if board[j][i] not in hc or board[j][i]==".":
                    hc[board[j][i]]=1
                else:
                    return False
            hr={}
            hc={}
        for i in (0, 3, 6):
         for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not self.is_unit_valid(square):
                return False
        return True
        
    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
        

s=Solution()
print(s.isValidSudoku( board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","5","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))