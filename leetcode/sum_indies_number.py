class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        for i in range(0, len(nums)):
            val = bin(i)
            if val.count("1") == k:
                sum += nums[i]
        print(sum)


s = Solution()
s.sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1)
