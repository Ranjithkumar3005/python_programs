class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        dp = [0] * n

        for i in range(n - 1):
            if (nums[i] % 2 and nums[i + 1] % 2) or (
                not nums[i] % 2 and not nums[i + 1] % 2
            ):
                dp[i + 1] = dp[i] - 1
            else:
                dp[i + 1] = dp[i] + 1

        res = []
        for f, t in queries:
            res.append(t - f == dp[t] - dp[f])

        return res


s = Solution()
s.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]])
