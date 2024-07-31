class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1=0
        sum2=0
        
        for i in nums:
            if i<10:
                sum1+=i
            else:
                sum2+=i
        if sum1==sum2:
            return False
        return True
        

s=Solution()
print(s.canAliceWin(nums = [1,2,3,4,5,14]))