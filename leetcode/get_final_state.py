class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        i = 0
        while i < k:
            min1 = min(nums)
            indx = nums.index(min1)
            nums[indx] *= multiplier
            i += 1
        print(nums)


s = Solution()
s.getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2)
