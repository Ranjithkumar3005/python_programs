class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        max_sum = current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]

        max_sum = max(max_sum, current_sum)
        return max_sum

# Example usage:
s = Solution()
print(s.maxAscendingSum(nums = [20, 10]))  # Output: 20
