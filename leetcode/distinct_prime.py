class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def prime_factors(n):
            factors = []
    
            while n % 2 == 0:
                factors.append(2)
                n = n // 2
    
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    factors.append(i)
                    n = n // i
    
            if n > 2:
                factors.append(n)
    
            return factors
        distinct_primes = set()
        for num in nums:
            distinct_primes.update(prime_factors(num))
        
        return len(distinct_primes)





s=Solution()
s.distinctPrimeFactors( nums = [2,4,3,7,10,6])