class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            nums[i]=nums[i]*nums[i]
        nums=sorted(nums)
        return nums
        
        
s=Solution()
print(s.sortedSquares(nums = [-7,-3,2,3,11]))