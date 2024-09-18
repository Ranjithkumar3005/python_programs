import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            max1 = max(gifts)  # Find the maximum value in gifts
            idx = gifts.index(max1)  # Find the index of the maximum value
            gifts[idx] = math.floor(math.sqrt(max1))  # Replace the max value with its square root
            
        return sum(gifts)  # Return the sum of the modified gifts list

s = Solution()
print(s.pickGifts(gifts=[25, 64, 9, 4, 100], k=4))  # Example test case
