class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ind1=0
        ind2=0
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j]=="R":
                    ind1=i
                    ind2=j
        c=0
        top=ind1
        bottom=ind1
        left=ind2
        right=ind2
        dum=0
        print(ind1,ind2)
        while True:
                top-=1
                if top<0:
                    break
                if board[top][ind2]=="B":
                    break
                if board[top][ind2]=="p":
                    c+=1
                    break
        while True:
                bottom+=1
                if board[bottom][ind2]=="B":
                    break
                if board[bottom][ind2]=="p":
                    c+=1
                    break
                if bottom==len(board)-1:
                    break
        while True:
                left-=1
                if left<0:
                    break
                if board[ind1][left]=="B":
                    break
                if board[ind1][left]=="p":
                    c+=1
                    break
                
        while True:
                right+=1
                if board[ind1][right]=="B":
                    break
                if board[ind1][right]=="p":
                    c+=1
                    break
                if right==len(board[0])-1:
                    break
        print(c)
s=Solution()
s.numRookCaptures([["R",".","p",".","p",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],["p",".",".",".",".",".",".","."],["p",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])