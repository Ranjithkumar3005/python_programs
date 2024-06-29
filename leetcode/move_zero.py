class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
        print(nums)
        
        
s=Solution()
s.moveZeroes(nums = [0,1,0,3,12])