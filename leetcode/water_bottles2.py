class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
        d=numBottles
        fb=0
        eb=numBottles
        while True:
            if eb>=numExchange:
                eb-=numExchange
                numExchange+=1
                fb+=1
            else:
                eb+=fb
                d+=fb
                fb=0
            if fb==0 and eb<numExchange:
                break
        print(d)
        

s=Solution()
s.maxBottlesDrunk( numBottles = 1, numExchange = 1)