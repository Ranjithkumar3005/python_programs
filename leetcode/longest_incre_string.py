import math
class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = math.floor((i + j) / 2)
                print(m)
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

        
s=Solution()
print(s.lengthOfLIS(nums =[0,1,0,3,2,3]))