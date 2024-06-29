class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        max=-1
        nums=sorted(nums)
        for i in nums:
            if i<0:
                h[abs(i)]=1
            elif i in h:
                max=i
        print(max)
                      
s=Solution()
s.findMaxK([-9,-43,24,-23,-16,-30,-38,-30])