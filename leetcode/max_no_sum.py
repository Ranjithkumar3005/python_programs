class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]+nums[1]
        c=1
        
        for i in range(2,len(nums),2):
            if i==len(nums)-1:
                break
            if nums[i]+nums[i+1]==sum:
                c+=1
            else:
                break
        print(c)
            
        
        
        

s=Solution()
s.maxOperations( nums = [3,2,6,1,4])