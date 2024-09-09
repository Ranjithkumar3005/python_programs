class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        pre_sum = [0] * n 
        suf_sum = [0] * n 
        pre_sum[0] = nums[0]
        for i in range(1, n):
            pre_sum[i] = max(pre_sum[i - 1], nums[i])
        
        suf_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suf_sum[i] = min(suf_sum[i + 1], nums[i])
        
        total_sum = 0
        for i in range(1, n - 1):
            if pre_sum[i - 1] < nums[i] < suf_sum[i + 1]:
                total_sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_sum += 1
        
        print(total_sum)

s = Solution()
s.sumOfBeauties([1, 2, 3]) 