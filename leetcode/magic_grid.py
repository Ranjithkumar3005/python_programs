class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c=0
        dum=[]
        if len(grid)<3 or len(grid[0])<3:
            return 0
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[0])-2):
                dumm=[]
                for m in range(i,i+3):
                    d=[]
                    for n in range(j,j+3):
                        d.append(grid[m][n])
                    dumm.append(d)
                dum.append(dumm)
        
        for i in range(0,len(dum)):
            check=False
            for m in range(0,3):
                sum=0
                for n in range(0,3):
                    if dum[i][m][n]>9 or dum[i][m][n]<1:
                        check=True
                        break
                    sum+=dum[i][m][n]
                if sum!=15:
                    check=True
                    break
                
            if not check:
                for p in range(0,3):
                 sum=0
                 for q in range(0,3):
                    if dum[i][q][p]>9 or dum[i][q][p]<1:
                        check=True
                        break
                    sum+=dum[i][q][p]
                 if sum!=15:
                        check=True
                        break
                 
            if (dum[i][0][0]+dum[i][1][1]+dum[i][2][2])!=15 or (dum[i][0][2]+dum[i][1][1]+dum[i][2][0])!=15:
                check=True
            if not check:
                c+=1
        print(c)
s=Solution()
s.numMagicSquaresInside(grid = [[4,3,8,4]])