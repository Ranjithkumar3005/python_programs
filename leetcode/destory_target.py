class Solution(object):
    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        HashMap={}
        for i in nums:
            val=(i % space)
            if val in HashMap:            
                HashMap[val] += 1
            else:
                HashMap[val]=1
        res = max(HashMap.values())
        
        for i in sorted(nums):
            if HashMap[i % space] == res:
                return i
        
        

s=Solution()
print(s.destroyTargets(nums = [3,7,8,1,1,5], space = 2))