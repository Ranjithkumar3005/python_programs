class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        dum=[]
        c=0
        strs=""
        for i in range(0,len(s)):
            if c!=k:
                strs+=s[i]
                c+=1
            if c==k:
                dum.append(strs)
                c=0
                strs=""
        if len(s)%k!=0:
            m=len(s)%k
            strs=""
            strs+=s[len(s)-m:len(s)]
            for i in range(0,k-m):
                strs+=fill
            dum.append(strs)
        print(dum)
s=Solution()
s.divideString(  s = "ctoyjrwtngqwt", k = 8, fill = "n")