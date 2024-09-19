class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        # For a valid original array to exist:
        # The length of the `derived` array must be even
        # because the length of the original array `A` will be
        # length of `derived` + 1
        n = len(derived)
        
        if n == 1:
            # For a single element, the original array always exists (either [0] or [1])
            return True
        
        # Check if derived is a valid XOR transformation array
        # Check if the XOR of all elements in derived is 0
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        
        return xor_sum == 0

s = Solution()
print(s.doesValidArrayExist(derived = [1,1,0]))  # Expected output: True
print(s.doesValidArrayExist(derived = [1,0,1]))  # Expected output: False
