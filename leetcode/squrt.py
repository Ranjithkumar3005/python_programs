class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        count=1
        while i!=0:
            count+=1
            val=self.checking(val/count)
        return val
        
s=Solution()
s.mySqrt(8)