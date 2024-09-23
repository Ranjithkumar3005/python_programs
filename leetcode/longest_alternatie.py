class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max1 = 0
        for i in range(0, len(nums)):
            if nums[i] < threshold and nums[i] % 2 == 0:
                c = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] > threshold or nums[j] % 2 == nums[j - 1] % 2:
                        break
                    else:
                        c += 1
                max1 = max(max1, c)
        print(max1)


s = Solution()
s.longestAlternatingSubarray(nums=[3, 2, 5, 4], threshold=5)
