class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tot = 0
        max_sum = 0
        h = {}
        left = 0
        
        for right in range(len(nums)):
            if nums[right] in h:
                h[nums[right]] += 1
            else:
                h[nums[right]] = 1
            tot += nums[right]
            
            if right - left + 1 > k:
                h[nums[left]] -= 1
                tot -= nums[left]
                if h[nums[left]] == 0:
                    del h[nums[left]]
                left += 1
            
            if right - left + 1 == k and len(h) == k:
                max_sum = max(max_sum, tot)
        
        return max_sum

s = Solution()
print(s.maximumSubarraySum(nums = [1,5,4,2,9,9,9,4,5,2], k = 3))
