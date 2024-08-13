class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                count_name = 0
                count_typed = 0
                
                # Count occurrences of the current character in name
                while i < len(name) and name[i] == name[i - count_name]:
                    count_name += 1
                    i += 1
                
                # Count occurrences of the current character in typed
                while j < len(typed) and typed[j] == typed[j - count_typed]:
                    count_typed += 1
                    j += 1
                
                # Check if typed has at least as many occurrences as name
                if count_typed < count_name:
                    return False
            else:
                return False
        
        # Ensure we have consumed all characters in both name and typed
        return i == len(name) and j == len(typed)

s = Solution()
print(s.isLongPressedName(name="alex", typed="aaleex"))  # Expected output: True
print(s.isLongPressedName(name="alex", typed="aaleexx")) # Expected output: False
