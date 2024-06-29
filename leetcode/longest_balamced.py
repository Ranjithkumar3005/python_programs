class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        zero=0
        one=0
        onecomes=False
        zerocomes=False
        for i in range(0,len(s)):
            if s[i]=='0':
             zero+=1
             zerocomes=True
             if onecomes:
                 zero=1
                 onecomes=False
            else:
                one+=1
                onecomes=True
                if zerocomes:
                    one=1
                    zerocomes=False
        value=min(zero,one)
        return value*2
s=Solution()
print(s.findTheLongestBalancedSubstring("01111000"))