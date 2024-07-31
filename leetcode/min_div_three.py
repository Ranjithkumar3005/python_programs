class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        
        for i in range(0,len(nums)):
            if (nums[i]-1)%3==0 or (nums[i]+1)%3==0:
                c+=1
        print(c)
        
        

s=Solution()
s.minimumOperations(nums = [1,2,3,4])