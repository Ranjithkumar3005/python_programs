class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        val=set(nums[0])
        for i in range(1,len(nums)):
            diif=val-set(nums[i])
            val-=diif
        return val
        
        

s=Solution()
print(s.intersection(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))