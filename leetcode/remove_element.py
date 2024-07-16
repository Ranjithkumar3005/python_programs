class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c=1
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]!=val:
                nums[c] = nums[i]
                c+=1
        return (c)
        
        

s=Solution()
print(s.removeElement(nums = [3,2,2,3], val = 3))