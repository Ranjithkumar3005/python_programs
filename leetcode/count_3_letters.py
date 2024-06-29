class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3: 
           return s
        result = '';
        for i in range(0,len(s)):
            if (i > 1 and s[i - 2] == s[i - 1] and s[i - 1] == s[i]):
                 continue;
        
            result += s[i];
        print(result)
        
        
        
s=Solution()
s.makeFancyString(s = "aaabaaaa")