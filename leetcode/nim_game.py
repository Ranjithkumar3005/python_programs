class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=3:
            return True
        
        if n>7:
            return True
        return False
        
        

s=Solution()
s.canWinNim(n = 4)