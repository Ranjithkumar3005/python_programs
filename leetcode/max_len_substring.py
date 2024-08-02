class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max1=0
        
        h={}
        for i in range(0,len(s)):
            c=1
            h[s[i]]=1
            for j in range(i+1,len(s)):
                if s[j] in h:
                    h[s[j]]+=1
                else:
                    h[s[j]]=1
                c+=1
                if h[s[j]]>2:
                    c-=1
                    break
            
            max1=max(max1,c)
            h={}
        max1=max(max1,c)
        print(max1)

s=Solution()
s.maximumLengthSubstring( s ="aaaa")