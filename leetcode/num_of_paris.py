class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        
        c=0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)): 
                if i != j and nums[i] + nums[j] == target: 
                    c += 1
        return c 
        

s=Solution()
print(s.numOfPairs(nums = ["777","7","77","77"], target = "7777"))