class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0  # to track how many elements need to be removed
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                count += 1
                if count > 1:
                    return False
                
                # Check if removing nums[i-1] or nums[i] would make the sequence strictly increasing
                if i > 1 and nums[i] <= nums[i-2]:
                    nums[i] = nums[i-1]  # simulate removing nums[i]
        
        return True

s=Solution()
s.canBeIncreasing()