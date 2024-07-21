class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={}
        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        for i in h:
            if h[i]>=3:
                if h[i]%2==0:
                    h[i]=2
                else:
                    h[i]=1
        tot=0
        for i in h:
            tot+=h[i]
        print(tot)
        
s=Solution()
s.minimumLength( s = "aa")