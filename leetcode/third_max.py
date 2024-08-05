class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        nums=sorted(nums,reverse=True)
        if len(nums)<3:
            return nums[0]
        return nums[2]
        
        

s=Solution()
print(s.thirdMax(nums = [-2147483648, 1, 2]))