class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in nums:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        max1 = max(h.values())
        val1 = len(nums) - max1
        tot = max1 - val1
        if tot > 0:
            return tot
        return 0


s = Solution()
print(s.minLengthAfterRemovals(nums=[1, 1, 2, 2, 3, 3]))
