class Solution():
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=float(abs(n))
        
        while True:
            n=n/4
            print(n)
            if n==1:
                break
            if n<4 and n!=1:
                return False
        return True
        

s=Solution()
print(s.isPowerOfFour(1))
        