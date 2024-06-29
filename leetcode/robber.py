class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1,rob2=0,0
        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        print(rob2)
            
                    
s=Solution()
s.rob(nums = [2,1,1,2])