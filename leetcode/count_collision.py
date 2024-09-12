class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        stack = []
        collisions = 0
        for d in directions:
            if d == 'R':
                stack.append('R')
                continue
            if d == 'L':
                if not stack:
                    continue
                collisions += 2 if stack[-1] == 'R' else 1
                stack.pop()
                d = 'S'
            if d == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                stack.append('S')
        return collisions

s = Solution()
print(s.countCollisions(directions = "RLRSLL"))  
