class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        else:
            if goal in s+s:
                return True
            else:
                return False
        
        
s=Solution()
print(s.rotateString( s = "abcde", goal = "abced"))