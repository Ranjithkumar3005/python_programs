class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
    
        for i in range(len(s)):
            if s[i] == '?':
                for char in 'abc': 
                    if (i == 0 or s[i-1] != char) and (i == len(s)-1 or s[i+1] != char):
                        s[i] = char
                        break
        return "".join(s)   

s=Solution()
print(s.modifyString(s = "?z?"))