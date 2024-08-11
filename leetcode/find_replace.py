class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # Create a list of tuples (index, source, target) and sort them by index
        replacements = sorted(zip(indices, sources, targets), reverse=True)
        print(replacements)
        for index, source, target in replacements:
            # Check if the substring matches the source
            if s[index:index+len(source)] == source:
                # Replace the source with the target
                s = s[:index] + target + s[index+len(source):]
        
        return s

# Example usage:
s = Solution()
result = s.findReplaceString(s="aaabcd", indices=[0, 2], sources=["aaa", "cd"], targets=["eee", "ffff"])
print(result)  # Output: "eeebffff"
