class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1=sorted(nums)
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == nums1:
                return True
        return False
        
        

s=Solution()
s.check(nums = [3,4,5,1,2])