class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(1,len(s),2):
            s = s[:i] + chr(ord(s[i-1])+int(s[i])) + s[i+1:]
        return s
        
        
s=Solution()
print(s.replaceDigits(s = "a1b2c3d4e"))