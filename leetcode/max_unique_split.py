class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if start == len(s):
                return len(seen)  # All substrings are processed, return the count

            max_count = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)  # Add new substring to the set
                    max_count = max(max_count, backtrack(end, seen))
                    seen.remove(substring)  # Backtrack and remove the substring

            return max_count

        return backtrack(
            0, set()
        )  # Start the recursion with an empty set of seen substrings
