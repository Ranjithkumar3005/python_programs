class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        dummy=s.split("|")
        for i in range(0,len(dummy),2):
            count+=dummy[i].count("*")
        print(count)
        

s=Solution()
s.countAsterisks(s = "yo|uar|e**|b|e***au|tifu|l")