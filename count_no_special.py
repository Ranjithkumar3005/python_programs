import math
class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        def sieve(n):
            is_prime = [True] * (n + 1)
            p = 2
            while (p * p <= n):
                if (is_prime[p] == True):
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            prime_list = [p for p in range(2, n + 1) if is_prime[p]]
            return prime_list
    
         # Get all primes up to sqrt(r)
        primes = sieve(int(math.sqrt(r)) + 1)
        special_count=0
        for prime in primes:
            square = prime * prime
            if l <= square <= r:
                special_count += 1
    
        total_numbers = r - l + 1
        not_special_count = total_numbers - special_count
    
        return not_special_count
        
        

s=Solution()
print(s.nonSpecialCount( l = 4, r = 16))