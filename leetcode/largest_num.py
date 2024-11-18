class Solution:
    def largestNumber(self, num):
        num = list(num)  # Convert to a list for easy manipulation
        n = len(num)

        # Helper function to sort a segment in descending order
        def sort_segment(start, end):
            segment = sorted(num[start : end + 1], reverse=True)
            num[start : end + 1] = segment

        i = 0
        while i < n:
            j = i
            while j + 1 < n and (int(num[j]) % 2 == int(num[j + 1]) % 2):
                j += 1
            # Sort this segment in descending order
            sort_segment(i, j)

            i = j + 1

        return "".join(num)


# Example Usage:
sol = Solution()
print(sol.largestNumber("7596801"))  # Expected output: "9876501"
