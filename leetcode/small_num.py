class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        n = len(pattern)
        result = []
        stack = []
        for i in range(1, n + 2):
            stack.append(str(i))
            if i == n + 1 or pattern[i - 1] == "I":
                while stack:
                    result.append(stack.pop())

        return "".join(result)  # Join list into a string and return


# Example usage
s = Solution()
print(s.smallestNumber(pattern="IIIDIDDD"))  # Output: "12354876"
