class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h={}
        
        for i in range(0,len(nums)):
            c=0
            h[i]=0
            for j in range(i,len(nums)):
                if nums[j]%2!=0:
                    c+=1
                if c>k:
                    break
                if c==k:
                    h[i]+=1
        d=0
        
        for i in h:
            d+=h[i]
        return d
        
s=Solution()
s.numberOfSubarrays(nums = [2,4,6], k = 1)