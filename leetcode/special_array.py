class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        for i in range(0,len(nums)-1):
             if ((nums[i]%2==0) and nums[i+1]%2!=0) or ((nums[i]%2!=0) and nums[i+1]%2==0):
                 continue
             else:
                 return False
        return True
        

s=Solution()
print(s.isArraySpecial( nums = [4,3,1,6]))