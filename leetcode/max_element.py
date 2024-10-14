import heapq
import math


class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-x for x in nums]
        heapq.heapify(nums)

        tot = 0
        while k > 0:
            largest = -heapq.heappop(nums)
            tot += largest

            new_value = math.ceil(largest / 3)
            heapq.heappush(nums, -new_value)

            k -= 1
        print(tot)


s = Solution()
s.maxKelements(nums=[1, 10, 3, 3, 3], k=3)
