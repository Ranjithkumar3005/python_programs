class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        dum=[]
        for i in range(0,len(nums)):
            dum.insert(index[i],nums[i])
        print(dum)


s=Solution()
s.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])