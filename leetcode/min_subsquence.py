class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=sorted(nums,reverse=True)
        total_sum = sum(nums)
        dum=[]
        dum_sum=0
        for i in range(0,len(nums)):
            dum_sum+=nums[i]
            dum.append(nums[i])
            if dum_sum>total_sum-dum_sum:
                break
        print(dum)
        
        
        

s=Solution()
s.minSubsequence(nums = [4,4,7,6,7])