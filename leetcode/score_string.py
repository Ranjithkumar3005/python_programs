class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        tot=0
        for i in range(0,len(s)-1):
            tot+=abs(ord(s[i])-ord(s[i+1]))
        print(tot)
        
        
s=Solution()
s.scoreOfString("zaz")