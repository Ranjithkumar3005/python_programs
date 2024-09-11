class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        return bin(start^goal).count("1")
        
        
s=Solution()
print(s.minBitFlips(start = 3, goal = 4))