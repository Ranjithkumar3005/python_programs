class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums);

        pre , suff = 1,1
        ans = -2147483648
        for i in range(0,n) :
            if (pre == 0): pre = 1
            if (suff == 0): suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, max(pre, suff))
        
        return ans

s=Solution()
s.maxProduct(nums = [-2,3,-4])