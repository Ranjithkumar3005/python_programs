class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k & ~n != 0:
           return -1
        
    # Count the number of 1 bits in n that need to be turned to 0
        print(n & ~k)
        changes_needed = bin(n & ~k).count('1')
    
        return changes_needed
        
s=Solution()
print(s.minChanges( n = 13, k = 4))