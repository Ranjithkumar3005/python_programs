class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total_sum = sum(cardPoints)
    
        if k == n:
            return total_sum
        
        window_sum = sum(cardPoints[:n - k])
        min_window_sum = window_sum
        for i in range(n - k, n):
            window_sum = window_sum - cardPoints[i - (n - k)] + cardPoints[i]
            min_window_sum = min(min_window_sum, window_sum)
    
        return total_sum - min_window_sum
        

s=Solution()
s.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)