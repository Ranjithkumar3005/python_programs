class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        val=str(bin(n))
        c=val.count("1")
        print(c)
        
        

s=Solution()
s.hammingWeight(n=11)