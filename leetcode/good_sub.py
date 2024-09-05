class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        for i in range(0,len(s)-2):
            h={}
            for j in range(i,i+3):
                h[s[j]]=1
            print(h)
            if len(h)==3:
                c+=1
        print(c)

s=Solution()
s.countGoodSubstrings(s = "aababcabc")