class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        
        if len(nums)==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permuteUnique(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return set(res)
        
        


s=Solution()
print(s.permuteUnique( nums = [1,1,2]))