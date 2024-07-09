class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        first=0
        tot=0
        
        for i in range(0,len(customers)):
            if first<customers[i][0]:
                first=customers[i][0]
            tot+=(first+customers[i][1]-customers[i][0])
            first=first+customers[i][1]
            print(tot)
        print(round(tot/len(customers)))
        
        



s=Solution()
s.averageWaitingTime(customers = [[5,2],[5,4],[10,3],[20,1]])
  