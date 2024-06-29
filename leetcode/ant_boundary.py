class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        d=0
        for i in range(0,len(nums)):
            if nums[i]>=0:
                c+=nums[i]
            elif nums[i]<0:
                c+=nums[i]
            if c==0:
                d+=1
        print(d)
        
s=Solution()
s.returnToBoundaryCount(nums = [2,3,-5])