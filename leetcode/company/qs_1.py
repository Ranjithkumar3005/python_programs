class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        for i in range(0,len(nums)):
            if target<nums[i]:
                return i-1
        return len(nums)
        

s=Solution()
print(s.searchInsert(nums = [1,3,5,6], target = 5))