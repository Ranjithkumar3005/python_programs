class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rows, cols = len(points), len(points[0])
        dp = points[0][:] 
        print(dp)
        
        for i in range(1, rows):
            new_dp = [0] * cols
            left = [0] * cols
            right = [0] * cols
            
            left[0] = dp[0]
            for j in range(1, cols):
                left[j] = max(left[j-1] - 1, dp[j])
            print("left",left)
            right[-1] = dp[-1]
            for j in range(cols-2, -1, -1):
                right[j] = max(right[j+1] - 1, dp[j])
            print("right",right)
            for j in range(cols):
                new_dp[j] = points[i][j] + max(left[j], right[j])
            print("new",new_dp)
            dp = new_dp 
        
        return max(dp)
        
s = Solution()
print(s.maxPoints(points=[[1,2,3],[1,5,1],[3,1,1]])) 
