class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1=max(nums)
        return nums.index(num1)
        
        

s=Solution()
print(s.findPeakElement(nums = [1,2,3,1]))