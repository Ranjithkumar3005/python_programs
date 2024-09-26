class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Separate characters at even and odd indices
        even_s1 = [s1[i] for i in range(0, len(s1), 2)]
        odd_s1 = [s1[i] for i in range(1, len(s1), 2)]

        even_s2 = [s2[i] for i in range(0, len(s2), 2)]
        odd_s2 = [s2[i] for i in range(1, len(s2), 2)]

        # Check if the sorted lists of even and odd characters match
        return sorted(even_s1) == sorted(even_s2) and sorted(odd_s1) == sorted(odd_s2)


# Test cases
s = Solution()
print(s.checkStrings(s1="abcdba", s2="cabdab"))  # Output: True
