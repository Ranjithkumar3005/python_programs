import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1=str(x)
        length=len(x1)
        va=True
        for i in range(0,int(math.floor(length/2))):
            if x1[i]==x1[(length-1)-i]:
                va=("True")
            else:
                print("Flase")
        print(va)
s=Solution()
s.isPalindrome(1000021)