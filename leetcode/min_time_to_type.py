class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        tot = min(abs(ord(word[0]) - ord("a")), 26 - abs(ord(word[0]) - ord("a")))

        tot += 1

        for i in range(len(word) - 1):
            val1 = ord(word[i]) - ord("a")
            val2 = ord(word[i + 1]) - ord("a")

            # Calculate both clockwise and counterclockwise distances
            direct_dist = abs(val2 - val1)
            wrap_around_dist = 26 - direct_dist

            # Add the minimum of the two distances
            tot += min(direct_dist, wrap_around_dist)

            # Add 1 second for typing each character
            tot += 1

        return tot


# Example usage
s = Solution()
print(s.minTimeToType("bza"))  # Expected output: 7
