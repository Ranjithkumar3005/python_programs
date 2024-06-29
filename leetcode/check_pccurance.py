class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        dum=sorted(list(h.values()))
        if len(dum)==1:
            return True
        elif dum[0]==dum[len(dum)-1]:
            return True
        return False
        
        
        
s=Solution()
s.areOccurrencesEqual( s = "abacbc")