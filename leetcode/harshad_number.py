class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1=str(x)
        
        sum=0
        for i in range(0,len(str1)):
            sum+=int(str1[i])
        
        if x%sum==0:
            return sum
        return -1
        
        

s=Solution()
s.sumOfTheDigitsOfHarshadNumber(x = 18)