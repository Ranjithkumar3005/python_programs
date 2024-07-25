class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=""
        if s==s[::-1]:
            return s
        for i in range(0,len(s)):
            j=i
            k=len(s)-1
            while j<=k:
                st1=s[j:k+1]
                st2=st1[::-1]
                if st1==st2 and len(st)<len(st1):
                    st=st1
                k-=1
        
        print(st)
        
s=Solution()
print(s.longestPalindrome( "gbbb"))