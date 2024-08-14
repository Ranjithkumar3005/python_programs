class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=sorted(nums)
        dum=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                dum.append(nums[j]-nums[i])
        dum=sorted(dum)
        return dum[k-1]
        
        

s=Solution()
print(s.smallestDistancePair(nums = [1,3,1], k = 1))