class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        d=0
        max=0
        for i in range(0,len(s)):
            if d==len(t):
                return 0
            if s[i]==t[d]:
                d+=1
        if max<d:
                    max=d
        print(len(t)-max)
        
s=Solution()
s.appendCharacters(s = "vrykt", t = "rkge")