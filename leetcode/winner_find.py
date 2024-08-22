class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner = arr[0]
        streak = 0
        
        for i in range(1, len(arr)):
            if winner > arr[i]:
                streak += 1
            else:
                winner = arr[i]
                streak = 1
            if streak == k:
                return winner
            
        return winner

s = Solution()
print(s.getWinner(arr = [3, 2, 1], k = 10))  # Expected output: 3
