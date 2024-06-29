class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        h={}
        s1=s.split(" ")
        print(s1)
        for i in range(0,len(pattern)):
            h[pattern[i]]=s1[i]
        dummy=""
        for i in range(0,len(pattern)):
            dummy+=h[pattern[i]]
        s=s.replace(" ","")
        if s==dummy:
            return True
        return False
        
s=Solution()
print(s.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))