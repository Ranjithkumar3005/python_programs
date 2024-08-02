class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if any(num >= k for num in nums):
            return 1

        n = len(nums)
        min_length = float('inf')

        for i in range(n):
            current_or = 0
            for j in range(i, n):
                current_or |= nums[j]
                if current_or >= k:
                    min_length = min(min_length, j - i + 1)
                    break

        return min_length if min_length != float('inf') else -1
        

s=Solution()
print(s.minimumSubarrayLength( nums = [16,1,2,20,32], k = 45))