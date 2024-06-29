import math


class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        h1={}
        h2={}
        c=0
        for i in range(0,math.floor(len(s)/2)):
            if s[i] not in h1:
                h1[s[i]]=1
            if s[len(s)-1-i] not in h2:
                h2[s[len(s)-1-i]]=1
            if h1!=h2:
                c+=1
        if len(s)==2 and c==1:
            return c+1
        if len(s)%2!=0:
           return c+1
        return c     
        

s=Solution()
print(s.minimumLength(s = "a"))