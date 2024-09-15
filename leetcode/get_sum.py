class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a1 = bin(a & 0xFFFFFFFF)[2:][::-1] 
        b1 = bin(b & 0xFFFFFFFF)[2:][::-1] 
        
        max_len = max(len(a1), len(b1))
        a1 = a1.ljust(max_len, '0')
        b1 = b1.ljust(max_len, '0')
        
        result = []
        carry = 0
        
        for i in range(max_len):
            bit_sum = int(a1[i]) + int(b1[i]) + carry
            
            if bit_sum == 2:
                result.append('0')
                carry = 1 
            elif bit_sum == 3:
                result.append('1')
                carry = 1 
            else:
                result.append(str(bit_sum)) 
                carry = 0
        
        if carry:
            result.append('1')
        
        binary_str = ''.join(result[::-1])
        result_int = int(binary_str, 2)
        
        if result_int > 0x7FFFFFFF:
            result_int -= 0x100000000
        
        return result_int

s = Solution()
print(s.getSum(a = 2, b = 3))  # Output: 5
