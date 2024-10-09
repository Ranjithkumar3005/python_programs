class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        count_0 = 0
        count_1 = 0
        total = 0

        for end in range(len(s)):
            # Update counts based on the current character
            if s[end] == "0":
                count_0 += 1
            else:
                count_1 += 1

            # Shrink window until both counts are <= k
            while count_0 > k and count_1 > k:
                if s[start] == "0":
                    count_0 -= 1
                else:
                    count_1 -= 1
                start += 1

            # All substrings from start to end are valid
            total += end - start + 1

        return total
