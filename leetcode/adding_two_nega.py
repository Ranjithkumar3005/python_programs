class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry != 0:
            digit1 = arr1[i] if i >= 0 else 0
            digit2 = arr2[j] if j >= 0 else 0
            
            # Calculate the sum of the current digits and carry
            total = digit1 + digit2 + carry
            # Add the current bit to the result
            result.append(total & 1)
            # Calculate the carry for the next bit
            carry = -(total >> 1)
            
            i -= 1
            j -= 1
        
        # Remove leading zeros if necessary
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Reverse the result to get the correct order
        result.reverse()
        return result

# Example usage:
s = Solution()
print(s.addNegabinary([1, 1, 1, 1, 1], [1, 0, 1]))  # Output: [1, 0, 0, 0, 0]
