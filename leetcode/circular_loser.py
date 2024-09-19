class Solution:
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        received = set()  # To keep track of friends who have received the ball
        current = 1  # Start with friend 1
        step = 1  # The step size increases with each pass
        
        while current not in received:
            received.add(current)
            # Calculate the next friend to receive the ball
            current = (current + step * k - 1) % n + 1
            step += 1
        
        # Determine losers: friends who did not receive the ball
        all_friends = set(range(1, n + 1))
        losers = list(all_friends - received)
        return sorted(losers)

# Example usage
s = Solution()
print(s.circularGameLosers(n = 4, k = 4))  # Example output: [2, 3]
