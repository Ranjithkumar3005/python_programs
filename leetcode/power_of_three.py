class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tot=abs(n)
        i=0
        if n==-1:
            return False
        while True:
            if 3**i==n:
                return True
            if 3**i>n:
                return False
            i+=1
        

s=Solution()
print(s.isPowerOfThree(0))