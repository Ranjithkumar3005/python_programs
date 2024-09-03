class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        h={}
        
        for i in range(0,len(logs)):
            if logs[i][0] in h:
                h[logs[i][0]][logs[i][1]]=1
            else:
                h[logs[i][0]]={logs[i][1]:1}
        dum=[0]*k
        for i in h:
            dum[len(h[i])-1]+=1
        print(dum)
        
        

s=Solution()
s.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5)