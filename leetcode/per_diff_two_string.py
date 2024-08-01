class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sum=0
        
        for i in range(0,len(s)):
            v2=t.index(s[i])
            
            sum+=abs(i-v2)
        print(sum)
        
        

s=Solution()
s.findPermutationDifference( s = "abcde", t = "edbac")