class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        original_n = n
        multiplier = 1
        
        while True:
            digit_sum = sum(int(digit) for digit in str(n))
            if digit_sum <= target:
                return n - original_n  
            n = ((n // (10 ** multiplier)) + 1) * (10 ** multiplier)
            multiplier += 1

s = Solution()
print(s.makeIntegerBeautiful(n=16, target=6))
