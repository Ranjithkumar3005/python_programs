class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0,len(s)-1):
            dum=(s[i]+s[i+1])[::-1]
            if dum in s:
                return True
        return False
        
        

s=Solution()
print(s.isSubstringPresent(s = "abcba"))