class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        nums.sort()
        result=0
        start,end=len(nums)-1,len(nums)-1
        for i in range(len(nums)):
            while end >=0 and nums[i]+nums[end]>upper:
                end-=1
            while start>=0 and nums[i]+nums[start]>=lower:
                start-=1
            if(start < i and end >= i):
                result+=end-start-1
            else:
                result+=end-start
        return result/2
        

s=Solution()
print(s.countFairPairs( nums = [0,1,7,4,4,5], lower = 3, upper = 6))