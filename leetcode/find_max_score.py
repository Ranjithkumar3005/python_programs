class Solution(object):
    def findMaximumScore(nums):
        n = len(nums)
        idx = 0
        l = nums[0]
        ans = 0

        for i in range(1, n):
            if nums[i] > l:
                k = i - idx
                ans += l * k
                l = nums[i]
                idx = i

        k = n - 1 - idx
        ans += l * k

        return ans


s = Solution()
s.findMaximumScore(nums=[4, 3, 1, 3, 2])
