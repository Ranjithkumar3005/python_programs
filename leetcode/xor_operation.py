class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
        xor_sum = start
        for i in range(1, n):
            xor_sum ^= (start + 2 * i)
        
        return xor_sum
        
        

s=Solution()
print(s.xorOperation(n = 5, start = 0))