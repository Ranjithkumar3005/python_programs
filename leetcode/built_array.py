class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dum=[]
        
        for i in nums:
            dum.append(nums[i])
        print(dum)
        
        

s=Solution()
s.buildArray(nums = [0,2,1,5,3,4])