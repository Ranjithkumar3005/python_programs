class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        c = 1
        max = 1
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        for i in nums:
            if i in h:
                continue
            if i - 1 in h:
                c += 1
                h[i] = 1
            else:
                if max < c:
                    max = c
                h = {}
                c = 1
                h[i] = 1
        if max < c:
            max = c

        print(max)


s = Solution()
print(s.longestConsecutive([1, 2, 0, 4, 4]))
