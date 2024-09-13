class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        good_pairs = 0
        
        for i in range(len(nums)):
            transformed_value = i - nums[i]
            if transformed_value in h:
                good_pairs += h[transformed_value]
                h[transformed_value] += 1
            else:
                h[transformed_value] = 1
        
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        
        bad_pairs = total_pairs - good_pairs
        
        return bad_pairs
        
s = Solution()
print(s.countBadPairs(nums = [1, 2, 3, 4, 5]))