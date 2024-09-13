class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=0
        curr=0
        
        for i in nums:
            if i==0:
                curr+=1
                tot+=curr
            else:
                curr=0
                
        print(tot)
        

s=Solution()
s.zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4])