class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign=-1
        if (dividend<0) ^ (divisor<0):
            sign=-1
        else:
            sign=1
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        q=0
        while dividend>=divisor:
            dividend-=divisor
            q+=1
        
        if sign==-1:
            q=-q
        
        return q
        
s=Solution()
print(s.divide(dividend = 7, divisor = -3))