class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c=0
        if n==1:
            return True
        while True:
               if n%2!=0 or n==0:
                  return False
               n=self.check(n)
               c+=1
               if n==1:
                   return True
               if n==-1 and c%2==0:
                   return False
    def check(self,n):
        return n/2
        
s=Solution()
print(s.isPowerOfTwo(n = -1))