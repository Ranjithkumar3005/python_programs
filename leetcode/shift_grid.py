class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        final=grid.copy()
        while k!=0:
            dum=final.copy()
            for i in range(0,len(dum)-1):
                for j in range(1,len(dum)):
                    dum[i][j]=dum[i][j-1]
            for i in range(0,len(dum)):
                dum[i+1][0]=final[i+1][len(final)-1]
            dum[0][0]=final[len(final)-1][len(final[0])-1]
            final=dum.copy()
            k-=1
        print(final)
        
        #1260

s=Solution()
s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1)