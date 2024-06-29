class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            if i not in nums:
                return i
            i+=1
        return i
        
        
s=Solution()
print(s.missingNumber( nums = [0,1]))