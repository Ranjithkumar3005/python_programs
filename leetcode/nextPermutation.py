class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
         i -= 1
        # If no valid pivot is found, the array is in descending order
        if i >= 0:
          # Step 2: Find the smallest element larger than nums[i]
          j = len(nums) - 1
          while nums[j] <= nums[i]:
            j -= 1
        
          # Step 3: Swap
          nums[i], nums[j] = nums[j], nums[i]
    
        # Step 4: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
    
        return nums

        

s=Solution()
s.nextPermutation( nums = [1,2,3])