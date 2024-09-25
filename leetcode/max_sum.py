class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dum = []
        d = []
        for i in nums:
            str1 = str(i)
            ch = []
            for i in str1:
                ch.append(int(i))
            d.append(max(ch))
        max1 = max(d)
        for i in range(0, len(nums)):
            if d[i] == max1:
                dum.append(nums[i])
        if len(dum) <= 1:
            return -1
        dum = sorted(dum)
        return dum[-1] + dum[-2]


s = Solution()
print(s.maxSum([31, 25, 72, 79, 74]))
