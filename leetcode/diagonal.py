class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        dig1=[]
        dig2=[]
        n=len(nums)
        for i in range(0,n):
            dig1.append(nums[i][i])
            dig2.append(nums[i][n-i-1])
            
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        tot=dig1+dig2
        max1=0
        for i in tot:
            if is_prime(i):
                max1=max(max1,i)
        print(max1)


s=Solution()
s.diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]])