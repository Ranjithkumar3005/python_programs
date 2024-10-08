class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        tot=0
        for i in h:
            if h[i]==1:
                tot+=i
        return tot