class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        if len(p)==len(s):
            if p==s:
                return [0]
            else:
                return []
        h={}
        dum=[]
        for i in range(0,len(p)):
            if p[i] in h:
                h[p[i]]+=1
            else:
                h[p[i]]=1
                
        for i in range(0,len(s)-len(p)+1):
            h1={}
            h1[s[i]]=1
            for j in range(i+1,i+len(p)):
                if s[j] in h1:
                    h1[s[j]]+=1
                else:
                    h1[s[j]]=1
            if h==h1:
                dum.append(i)
        print(dum)

s=Solution()
s.findAnagrams(s = "abab", p = "ab")