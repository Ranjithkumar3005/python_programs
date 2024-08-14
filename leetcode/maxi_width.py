class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        max_width = 0

        # Create a decreasing stack of indices
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        # Traverse from right to left and find the maximum width ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width

# Example usage:
s = Solution()
print(s.maxWidthRamp(nums=[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))  # Output: 7
