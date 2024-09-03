class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=[]
        for i in range(0,len(s)):
            h1={}
            for j in range(i,len(s)):
                if s[j] in h1:
                    h1[s[j]]+=1
                else:
                    h1[s[j]]=1
                vals=h1.values()
                val1=max(vals)-min(vals)
                if val1!=0:
                   d.append(val1)
            
        print(sum(d))
s=Solution()
s.beautySum( s = "aabcb")