class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max1 = max(max1, nums[i] ^ nums[j])
        print(max1)


s = Solution()
s.maximumStrongPairXor(nums=[1, 2, 3, 4, 5])
