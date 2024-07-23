class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Initialize the position of the ball and the direction of movement
        position = 0
        direction = 1  # 1 means moving right, -1 means moving left
        
        # Simulate the movement of the ball for k seconds
        for _ in range(k):
            position += direction
            # Reverse direction if the ball reaches the end
            if position == 0 or position == n - 1:
                direction = -direction
        
        return position
        
        
s=Solution()
s.numberOfChild(n = 2, k = 4)