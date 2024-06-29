class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_sum = sum(nums)
        left, right = 0, total_sum
        result = []

        for i, n in enumerate(nums):
            right -= n
            result.append(n * i - left + right - n * (len(nums) - i - 1))
            left += n

        return result
        
        
s=Solution()
print(s.getSumAbsoluteDifferences(nums = [1,4,6,8,10]))