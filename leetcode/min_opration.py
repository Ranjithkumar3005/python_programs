class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(0,len(nums)-2):
            if nums[i]==0:
                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]  # Flip between 0 and 1
                nums[i + 2] = 1 - nums[i + 2]  # Flip between 0 and 1
                c += 1
       
        print(nums)    
        if 0 in nums:
            return -1
        return c

s=Solution()
print(s.minOperations( nums = [0,1,1,1,0,0]))