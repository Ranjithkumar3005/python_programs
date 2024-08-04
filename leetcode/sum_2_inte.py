class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
        # Calculate the carry and shift it left
            carry = a & b
            carry <<= 1
        # Calculate the sum without carry
            a = a ^ b
        
        # Update b to carry
            b = carry
        
        return a
        

s=Solution()
print(s.getSum(a = 19, b = 29))