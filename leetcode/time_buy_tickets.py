class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        t=0
        while tickets[k]!=0:
            for j in range(0,len(tickets)):
                if tickets[j]!=0:
                    t+=1
                    tickets[j]-=1
                if tickets[k]==0:
                    break
                    
        print(t)
                    
        
s=Solution()
s.timeRequiredToBuy(tickets = [84,49,5,24,70,77,87,8], k = 3)