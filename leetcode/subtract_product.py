class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        str1=str(n)
        pro=1
        sum=0
        for i in str1:
            pro*=int(i)
            sum+=int(i)
        return pro-sum



s=Solution()
s.subtractProductAndSum(n = 234)