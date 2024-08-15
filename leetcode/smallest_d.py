class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 1 % k
        length = 1
        
        while remainder != 0:
            remainder = (remainder * 10 + 1) % k
            length += 1
        
        return length
        
        

s=Solution()
print(s.smallestRepunitDivByK(k = 23))