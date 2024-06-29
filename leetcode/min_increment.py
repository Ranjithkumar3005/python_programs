class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        nums=sorted(nums)
        for i in range(1,len(nums)):
            tot+=nums[i]-nums[i-1]
        print(tot)

s=Solution()
s.minIncrementForUnique( nums = [500,400])