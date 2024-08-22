class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        dum=[]
        for i in nums:
            sum+=i
            dum.append(sum)
        print(dum)
        

s=Solution()
s.runningSum(nums = [1,2,3,4])