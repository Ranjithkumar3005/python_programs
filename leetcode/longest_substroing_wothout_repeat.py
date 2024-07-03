class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={}
        h1={}
        if len(s)==0:
            return 0
        for i in range(0,len(s)):
            c=0
            for j in range(i,len(s)):
                if s[j] not in h:
                    c+=1
                    h[s[j]]=1
                else:
                    break
            h1[i]=c
            h={}
        maxi=max(h1.values())
        return maxi
        
s=Solution()
print(s.lengthOfLongestSubstring(s = "a"))