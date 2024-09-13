class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        # If the counts of 'L', 'R', and '_' are not the same, return False
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Positions of 'L' and 'R' in start and target
        start_L = [i for i, c in enumerate(start) if c == 'L']
        start_R = [i for i, c in enumerate(start) if c == 'R']
        target_L = [i for i, c in enumerate(target) if c == 'L']
        target_R = [i for i, c in enumerate(target) if c == 'R']
        
        # Check 'L' positions: they should be able to move left
        for i in range(len(start_L)):
            if start_L[i] < target_L[i]:
                return False
        
        # Check 'R' positions: they should be able to move right
        for i in range(len(start_R)):
            if start_R[i] > target_R[i]:
                return False
        
        return True

# Example usage
s = Solution()
print(s.canChange(start = "_L__R__R_", target = "L______RR"))  # Output: True
