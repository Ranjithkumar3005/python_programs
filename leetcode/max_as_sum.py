class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        tot=nums[0]
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                tot+=nums[i+1]
            else:
                sum=max(sum,tot)
                tot=nums[i]
                
        print(sum)
        
        
        
s=Solution()
s.maxAscendingSum(nums = [10,20,30,5,10,50])