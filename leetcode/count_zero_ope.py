class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        c=0
        
        while num1!=0 and num2!=0:
            if num1>num2:
                num1-=num2
            else:
                num2-=num1
            c+=1
        print(c)

s=Solution()
s.countOperations(num1 = 2, num2 = 3)