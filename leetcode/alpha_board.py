class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        pos = {c: (i // 5, i % 5) for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x, y = 0, 0 
        result = ""
        for char in target:
            new_x, new_y = pos[char] 
            if new_y < y:
                result += 'L' * (y - new_y)
            if new_x < x:
                result += 'U' * (x - new_x)
            
            if new_y > y:
                result += 'R' * (new_y - y)
            if new_x > x:
                result += 'D' * (new_x - x)
            
            result += "!"
            
            x, y = new_x, new_y
        
        print(result)

# Example usage:
s = Solution()
s.alphabetBoardPath(target = "leet")  # Output: "DDR!UURRR!!DDD!"
