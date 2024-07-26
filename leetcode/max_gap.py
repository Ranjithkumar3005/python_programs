class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums=sorted(nums)
        max1=0
        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i] >max1:
                max1=nums[i+1]-nums[i] 
        print(max1)
        

s=Solution()
s.maximumGap( nums = [3,6,9,1])