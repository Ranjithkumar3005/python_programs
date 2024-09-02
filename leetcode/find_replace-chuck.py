class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        prefix = []
        total = 0
        for c in chalk:
            total += c
            prefix.append(total)
        
        k = k % total
        print(total)
        left, right = 0, len(prefix) - 1
        while left < right:
            mid = left + (right - left) // 2
            if prefix[mid] > k:
                right = mid
            else:
                left = mid + 1
        return left

s = Solution()
print(s.chalkReplacer(chalk=[5,1,5], k=22)) 
