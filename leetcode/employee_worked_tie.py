class Solution(object):
    def hardestWorker(self, n, logs):
        """
        :type n: int
        :type logs: List[List[int]]
        :rtype: int
        """
        max=0
        id=0
        for i in range(0,len(logs)):
            if i==0:
                max=logs[i][1]-0
                id=logs[i][0]
            if (logs[i][1]-logs[i-1][1]>max) or (logs[i][1]-logs[i-1][1]==max and id>logs[i][0]):
                max=logs[i][1]-logs[i-1][1]
                id=logs[i][0]
        print(id)
            
              
s=Solution()
s.hardestWorker(70,[[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]])