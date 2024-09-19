class Solution:
    def colorArray(self, n, queries):
        colors = [0] * n  
        answer = [] 
        adjacent_pairs = 0  
        def check_adjacent(index):
            """ Helper function to check adjacent pairs formed or broken """
            nonlocal adjacent_pairs
            if index > 0 and colors[index] == colors[index - 1] and colors[index] != 0:
                adjacent_pairs += 1
            if index < n - 1 and colors[index] == colors[index + 1] and colors[index] != 0:
                adjacent_pairs += 1
        
        def uncheck_adjacent(index):
            """ Helper function to uncheck adjacent pairs formed or broken """
            nonlocal adjacent_pairs
            if index > 0 and colors[index] == colors[index - 1] and colors[index] != 0:
                adjacent_pairs -= 1
            if index < n - 1 and colors[index] == colors[index + 1] and colors[index] != 0:
                adjacent_pairs -= 1
        
        for idx, color in queries:
            if colors[idx] != 0:
                uncheck_adjacent(idx)
            
            colors[idx] = color
            check_adjacent(idx)
            answer.append(adjacent_pairs)
        
        return answer

# Example usage:
sol = Solution()
n = 5
queries = [[1, 2], [2, 2], [3, 3], [2, 3]]
print(sol.colorArray(n, queries))  # Expected output: [0, 1, 1, 0]
