class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if prod in h:
                    h[prod] += 1
                else:
                    h[prod] = 1
        
        c = 0
        print(h)
        for count in h.values():
            if count > 1:
                c += (count * (count - 1)) // 2 * 8
        
        return c

s = Solution()
print(s.tupleSameProduct(nums=[1, 2, 4, 5, 10]))