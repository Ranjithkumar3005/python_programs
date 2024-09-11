class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        h1={}
        h2={}
        for i in s:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        for i in t:
            if i in h1:
                if h1[i]==1:
                    del h1[i]
                else:
                  h1[i]-=1
            else:
                if i in h2:
                   h2[i]+=1
                else:
                    h2[i]=1
        sum1=sum(h1.values())+sum(h2.values())
        print(sum1)
            

s=Solution()
s.minSteps( s = "leetcode", t = "coats")