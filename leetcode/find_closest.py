class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1=99999999
        val=0
        for i in nums:
            if min1>abs(i):
                val=i
                min1=abs(i)
            elif min1==abs(i):
                if val<0:
                    val=i
        print(val)
        

s=Solution()
s.findClosestNumber(nums = [-4,-1,-2,1,4,8])