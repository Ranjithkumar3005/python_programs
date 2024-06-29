class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        h={}
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] in h:
                    h[grid[i][j]]+=1
                else:
                    h[grid[i][j]]=1
        dummy=[]
        var=0
        for i in range(1,len(h)+2):
            if i not in h:
                var=i
                continue
            elif h[i]==2:
               dummy.append(i)
        dummy.append(var)
        print(dummy) 
        
s=Solution()
s.findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]])