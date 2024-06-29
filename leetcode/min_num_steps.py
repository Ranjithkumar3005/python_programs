class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        c=0
        for i in t:
            if i in h and h[i]!=0:
                h[i]-=1
            else:
                c+=1
        print(c)
s=Solution()
s.minSteps(s = "anagram", t = "mangaar")