class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sum = sum + nums[i]
            else:
                break

        while sum in nums:
            sum += 1
        return sum


s = Solution()
s.missingInteger(nums=[3, 4, 5, 1, 12, 14, 13])
