class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        
        i, j = 0, 0
        while i < len(start) and j < len(end):
            # Skip 'X' characters in both start and end
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1
            
            # If both pointers are at the end, return True
            if i == len(start) and j == len(end):
                return True
            
            # If one pointer has reached the end but the other hasn't
            if i == len(start) or j == len(end):
                return False
            
            # If the characters at the current positions do not match
            if start[i] != end[j]:
                return False
            
            # Check movement constraints
            if start[i] == 'L' and i < j:  # 'L' cannot move right
                return False
            if start[i] == 'R' and i > j:  # 'R' cannot move left
                return False
            
            # Move to the next character
            i += 1
            j += 1
        
        # After finishing the loop, ensure any remaining characters are 'X'
        while i < len(start):
            if start[i] != 'X':
                return False
            i += 1
        while j < len(end):
            if end[j] != 'X':
                return False
            j += 1
        
        return True
        
s=Solution()
print(s.canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))