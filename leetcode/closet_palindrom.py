class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        for i in range(0,1000000000000):
            temp = i
            reverse = 0
            while temp > 0:
                remainder = temp % 10
                reverse = (reverse * 10) + remainder
                temp = temp // 10
        
s=Solution()
s.nearestPalindromic(n = "123")