class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        c=0
        
        for i in range(0,len(startTime)):
            if queryTime>=startTime[i] and queryTime<= endTime[i]:
                c+=1
        print(c)
        
        
        

s=Solution()
s.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)