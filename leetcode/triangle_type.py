class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums)<3 or len(nums)>3:
            return None
        
        if nums[0]==nums[1] and nums[1]==nums[2]:
            return "equilateral"
        c=2
        for i in range(0,2):
            for j in range(i+1,3):
                sum=nums[i]+nums[j]
                if sum<nums[c]:
                    return "none"
                c-=1
        if (nums[0]==nums[1] and nums[1]!=nums[2]) or (nums[0]==nums[2] and nums[1]!=nums[2]) or (nums[1]==nums[2] and nums[0]!=nums[1]):
            return "isosceles"
        
        if (nums[0]!=nums[1] and nums[1]!=nums[2]):
            return "scalene"

s=Solution()
print(s.triangleType( nums = [2,3,5]))