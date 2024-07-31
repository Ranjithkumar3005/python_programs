class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)  # Convert string to a list of characters for easy manipulation
        n = len(s)
        
        # Iterate through the list of characters
        for i in range(n - 1):
            # Check if the current and next character have the same parity
            if (int(s[i]) % 2) == (int(s[i + 1]) % 2):
                # Swap if the next character is smaller than the current character
                if s[i + 1] < s[i]:
                    s[i], s[i + 1] = s[i + 1], s[i]
                    break  # Perform at most one swap and then exit the loop
        
        return "".join(s)

# Example usage
sol = Solution()
print(sol.getSmallestString("45320"))  # Output should be "43520"
