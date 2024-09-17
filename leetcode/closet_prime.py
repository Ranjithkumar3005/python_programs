class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2:
                return True  # 2 is the only even prime number
            if n % 2 == 0:
                return False  # eliminate all even numbers > 2

            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        primes=[]
        for i in range(left,right+1):
            if is_prime(i):
                primes.append(i)
        
        min1=9999999999
        vals=[-1,-1]
        for i in range(0,len(primes)-1):
            val1=primes[i+1]-primes[i]
            if val1<min1:
                min1=val1
                vals[0]=primes[i]
                vals[1]=primes[i+1]
        print(vals)
        
        
        

s=Solution()
s.closestPrimes(left = 10, right = 19)