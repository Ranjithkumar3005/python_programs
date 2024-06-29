class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=list(s)
        t1=list(t)
        for i in range(0,len(s)):
            s1[i]=t[i]
            t1[i]=s[i]
        s2=""
        t2=""
        for i in range(0, len(s1)):
            s2+=s1[i]
            t2+=t1[i]
        if s2==t and t2==s:
            return True
        return False
        
s=Solution()
print(s.isIsomorphic(s  = "foo", t = "bar"))