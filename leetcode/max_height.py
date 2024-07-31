class Solution:
    def maxHeightOfTriangle(self, red, blue):
        return max(self.helper(red, blue), self.helper(blue, red))
    
    def helper(self, red, blue):
        h = 0
        i = 1
        
        while True:
            if i % 2 == 1:
                if red >= i:
                    red -= i
                else:
                    break
            else:
                if blue >= i:
                    blue -= i
                else:
                    break
            h += 1
            i += 1
        
        return h

# Example usage
s = Solution()
print(s.maxHeightOfTriangle(red=2, blue=1))  # Output should be 2
