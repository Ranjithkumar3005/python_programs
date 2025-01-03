class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set()
        nums = sorted(nums)
        target = 0
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        print(output)


#

s = Solution()
print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
