class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                dum=nums[i-1]+1-nums[i]
                nums[i]+=dum
                c+=dum
    
        print(c)
        
        

s=Solution()
s.minOperations(nums = [1,5,2,4,1])