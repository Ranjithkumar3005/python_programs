class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        c = 0
        i = len(nums) - 1
        while i > 0:
            if nums[i] != nums[i - 1]:
                c+= len(nums) - i
            i -= 1
        
        print(c)
        
        

s=Solution()
s.reductionOperations( nums = [1,1,2,2,3])