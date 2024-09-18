class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[0]*len(nums)
        suf=[0]*len(nums)
        for i in range(0,len(nums)-1):
            pre[i+1]+=pre[i]+nums[i]
        
        for j in range(len(nums)-1,0,-1):
            suf[j-1]+=suf[j]+nums[j]
        
        dum=[]
        for i in range(0,len(nums)):
            dum.append(abs(pre[i]-suf[i]))
        return dum
        
        

s=Solution()
print(s.leftRightDifference(nums = [10,4,8,3]))