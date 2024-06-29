class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(0,len(grid)):
            arr1=[[0]*len(grid[i])]
            arr+=arr1
        for i in range(0,len(grid)):
            countr=0
            countr1=0
            countr0=0
            countc=0
            countc1=0
            countc0=0
            for j in range(0,len(grid[i])):
                countr+=1
                if grid[i][j]==1:
                    countr1+=1
                else:
                   countr0+=1
                if countr==len(grid[i]):
                    for l in range(0,len(grid[0])):
                        for k in range(0,len(grid)):
                            countc+=1
                            if grid[k][l]==1:
                               countc1+=1
                            else:
                               countc0+=1
                            if countc==len(grid):
                               total=countr1+countc1-countr0-countc0
                               arr[i][l]=total
                               countr=0
                               countc=0
                               countc1=0
                               countc0=0
        
        print(arr)
s=Solution()
s.onesMinusZeros( [[0,1,1],[1,0,1],[0,0,1]])