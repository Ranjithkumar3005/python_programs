class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=-1
        
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                 val=nums[j]-nums[i]
                 max1=max(max1,val)
                
        print(max1)
        
        

s=Solution()
s.maximumDifference(nums = [1,5,2,10])