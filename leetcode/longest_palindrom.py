class Solution(object):
    def longestPalindrome(self, s):
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
        c=0
        check=min(h.values())
        if check%2!=0:
            c+=check
        for i in h:
            if h[i]%2==0:
                c+=h[i]
        print(c)
        
s=Solution()
s.longestPalindrome( s = "bananas")