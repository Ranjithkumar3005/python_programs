class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        dum=[]
        for i in range(0,len(hours)):
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    dum.append([i,j])   
        return len(dum)     

s=Solution()
s.countCompleteDayPairs( hours = [12,12,30,24,24])