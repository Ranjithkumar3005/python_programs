class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        
        for i in nums:
            val = str(i)
            tot = sum(int(j) for j in val)
            if tot in h:
                h[tot][0] += i
                h[tot][1] += 1
            else:
                h[tot] = [i, 1]
        
        max1 = -1
        print(h)
        for total, (group_sum, count) in h.items():
            if count ==2:
                max1 = max(max1, group_sum)
        
        return max1

# Example usage
s = Solution()
print(s.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))  # Output: 54
