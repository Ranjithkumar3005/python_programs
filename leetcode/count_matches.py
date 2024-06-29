import math
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        while n>=2:
            if n%2!=0:
                n=math.floor((n/2))
                total+=n
                n+=1
                print(n)
            else:
                n=n/2
                total+=n
                print(n)
        print(int(total))
        
s=Solution()
s.numberOfMatches(2)