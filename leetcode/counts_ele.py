class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        sum=0
        for i in range(0,len(nums)):
            if nums[i] not in h:
                h[nums[i]]=1
            else:
                h[nums[i]]+=1
        max1=max(h.values())
        for i in h:
            if h[i]==max1:
                sum+=h[i]
        print(sum)                
        
s=Solution()
s.maxFrequencyElements(nums = [1,2,2,3,1,4])