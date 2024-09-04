class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min1=999999999
        for i in range(0,len(nums)):
            if nums[i]==target:
                min1=min(min1,abs(start-i))
        print(min1)
        

s=Solution()
print(s.getMinDistance(nums =[1,1,1,1,1,1,1,1,1,1], target = 1, start = 9))