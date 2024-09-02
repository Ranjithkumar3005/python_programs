class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
      
        tot = s.count("1")
        
        if tot % 3 != 0:
            return 0
        
        if tot == 0:
            n = len(s)
            return ((n - 1) * (n - 2) // 2) % MOD
        
        target = tot // 3
        
        first, second = 0, 0
        
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            
            if count == target:
                first += 1
            elif count == 2 * target:
                second += 1
            print(first,second)
        
        # The result is the product of the number of valid ways to make the two splits
        return (first * second) % MOD

s = Solution()
result = s.numWays(s="10101")
print(result)