import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        val=str(math.factorial(n))
        
        c=0
        for i in range(len(val)-1,-1,-1):
            if val[i]=="0":
                c+=1
            else:
                break
        return c
        
        
        

s=Solution()
s.trailingZeroes(n=5)