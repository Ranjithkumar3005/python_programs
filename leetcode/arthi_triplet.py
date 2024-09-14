class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[j] - nums[i] == diff:
                    for k in range(j + 1, n):
                        if nums[k] - nums[j] == diff:
                            cnt += 1
        
        return cnt
        

s=Solution()
s.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3)