class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_length = 0

        for key in freq:
            if key + 1 in freq:
                max_length = max(max_length, freq[key] + freq[key + 1])

        return max_length
