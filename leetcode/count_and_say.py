class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def loop(s):
            result = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(s[i - 1])
                    count = 1

            # Append the last group
            result.append(str(count))
            result.append(s[-1])

            return ''.join(result)

        current = "1"
        for _ in range(1, n):
            current = loop(current)
        
        return current

# Example usage
s = Solution()
print(s.countAndSay(4))  # Output: "1211"
