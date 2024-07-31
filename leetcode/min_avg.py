class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums=sorted(nums)
        dum=[]
        
        for i in range(0,len(nums)//2):
            avg=(nums[i]+nums[len(nums)-i-1])/2
            dum.append(float(avg))
        
        return float(min(dum))
        
        

s=Solution()
print(s.minimumAverage( nums = [7,8,3,4,15,13,4,1]))