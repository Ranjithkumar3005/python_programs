class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h1={}
        h2={}
        for i in s:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        for j in t:
            if j in h2:
                h2[j]+=1
            else:
                h2[j]=1
        dum=h1.values()
        dum1=h2.values()
        if dum==dum1:
            return True
        return False
        
        
        
s=Solution()
s.isIsomorphic(s = "egg", t = "add")