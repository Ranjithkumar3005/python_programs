class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = 0  # Counter for the position to place non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
        # After the loop, nums[:c] contains all elements except val
        return c
        
        

s=Solution()
print(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))