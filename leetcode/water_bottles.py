class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        tot=numBottles
        val1=numBottles
        while val1>=numExchange:
            val2=val1%numExchange
            val1=val1//numExchange
            tot+=val1
            val1+=val2
        print(tot) 
        
        

s=Solution()
s.numWaterBottles(numBottles = 9, numExchange = 3)