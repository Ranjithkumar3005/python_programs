class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        h = {}

        maxlength = 0
        for i in arr:
            val = i - difference
            if val in h:
                h[i] = h[val] + 1
            else:
                h[i] = 1
            maxlength = max(maxlength, h[i])
        print(maxlength)


s = Solution()
s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2)
