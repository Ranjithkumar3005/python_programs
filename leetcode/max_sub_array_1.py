class Solution:
    def findMaxAverage(self, nums, k):
        pre = 0
        max1 = 0

        for i in range(0, len(nums)):
            pre += nums[i]
            if i >= k - 1:
                max1 = max(max1, (float(pre) / k))
                pre -= nums[i - k + 1]
        return max1


s = Solution()
print(s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
