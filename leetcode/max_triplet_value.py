class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        l = [0] * n
        r = [0] * n
        s = nums[0]

        for i in range(1, n):
            l[i] = s
            s = max(s, nums[i])

        s = nums[n - 1]

        for i in range(n - 2, -1, -1):
            r[i] = s
            s = max(s, nums[i])

        for i in range(1, n - 1):
            k = (l[i] - nums[i]) * r[i]
            ans = max(ans, k)

        return ans


s = Solution()
print(s.maximumTripletValue(nums=[12, 6, 1, 2, 7]))
