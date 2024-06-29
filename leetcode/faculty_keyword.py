class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dummy=""
        for i in range(0,len(s)):
            if s[i]=="i":
                dummy=dummy[::-1]
            else:
                dummy+=s[i]
        return dummy
        
s=Solution()
print(s.finalString(s = "string"))