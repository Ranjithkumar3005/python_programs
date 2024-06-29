class Solution(object):
    def countPoints(self, r):
        """
        :type rings: str
        :rtype: int
        """
        ans = 0
        for i in range(10):
            i = str(i)
            if 'R'+i in r and 'G'+i in r and 'B'+i in r:
                ans += 1
        return ans
        
        
s=Solution()
print(s.countPoints("B0B6G0R6R0R6G9"))