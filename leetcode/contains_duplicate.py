class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h={}
        for i in nums:
            if i in h:
                return True
            else:
                h[i]=1
        return False
        
        
s=Solution()
print(s.containsDuplicate(nums = [1,2,3]))