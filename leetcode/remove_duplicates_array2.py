class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        insert_pos = 0

        for num in nums:
            # Allow up to two occurrences of each number
            if insert_pos < 2 or num > nums[insert_pos - 2]:
                nums[insert_pos] = num
                insert_pos += 1

        
        return insert_pos

s=Solution()
print(s.removeDuplicates( nums = [1,1,1,2,2,3]))