class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score=0
        for i in range(1,len(s)):
            dummy1=s[0:i]
            dummy2=s[i:len(s)]
            max=dummy1.count("0")+dummy2.count("1")
            if max_score<max:
                max_score=max
        print(max_score)
        
        
s=Solution()
s.maxScore(s = "111")