class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        c=0
        h={}
        tot=0
        if len(nums)==0 or len(nums)==1:
            return False
        h[0]=nums[0]
        for i in range(1,len(nums)):
            for j in h:
                if (h[j]+nums[i])%k==0:
                    return True
                else:
                    print(h)
                    h[j]+=nums[i]
            
            h[i]=nums[i]
        return False
        
s=Solution()
print(s.checkSubarraySum(nums = [23,2,4,6,7], k = 6))