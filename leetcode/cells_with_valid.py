class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        
        dum=[]
        for i in range(0,m):
            dum.append([0]*n)
        
        for i in indices:
            for j in range(0,len(dum[0])):
                dum[i[0]][j]+=1
            
            for k in range(0,len(dum)):
                dum[k][i[1]]+=1
            
        c=0
        for i in range(0,m):
            for j in range(0,n):
                if dum[i][j]%2!=0:
                    c+=1
        print(c)
s=Solution()
s.oddCells( m = 2, n = 3, indices = [[0,1],[1,1]])