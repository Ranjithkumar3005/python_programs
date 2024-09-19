class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        score1 = 0
        score2 = 0
        
        for i in range(len(player1)):
            # Check for player1 bonus based on previous 1 or 2 turns
            if i > 0 and player1[i - 1] >= 10:
                score1 += player1[i] * 2
            elif i > 1 and player1[i - 2] >= 10:
                score1 += player1[i] * 2
            else:
                score1 += player1[i]
                
            # Check for player2 bonus based on previous 1 or 2 turns
            if i > 0 and player2[i - 1] >= 10:
                score2 += player2[i] * 2
            elif i > 1 and player2[i - 2] >= 10:
                score2 += player2[i] * 2
            else:
                score2 += player2[i]
        
        # Print final scores for debugging
        print(score1, score2)
        
        # Return the result based on the scores
        if score1 > score2:
            return 1  # Player 1 wins
        elif score2 > score1:
            return 2  # Player 2 wins
        else:
            return 0  # Tie

# Example Test
s = Solution()
print(s.isWinner(player1 = [5, 10, 3, 2], player2 = [6, 5, 7, 3]))  # Expected output: 1 or 2 based on the scores
