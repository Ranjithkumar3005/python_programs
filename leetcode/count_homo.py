class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=1
        rol=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                rol+=1
                c+=(rol-1)
            else:
                rol=1
            c+=1
        print(c)   
        
        

s=Solution()
s.countHomogenous(s = "abbcccaa")