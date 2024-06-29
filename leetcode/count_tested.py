import numpy
class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        count=0
        d=numpy.array(batteryPercentages)
        for i in range(0,len(d)):
            if d[i]>0:
                count+=1
                d=d-1
        print(count) 
s=Solution()
s.countTestedDevices([0,1,2])