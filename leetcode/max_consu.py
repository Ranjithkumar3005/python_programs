class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        max1 = 0
        special = sorted(special) 
        max1 = max(max1, special[0] - bottom)
        
        for i in range(1, len(special)):
            max1 = max(max1, special[i] - special[i - 1] - 1)
        
        max1 = max(max1, top - special[-1])
        
        print(max1)

s = Solution()
s.maxConsecutive(bottom=2, top=9, special=[4, 6])  # Output: 2
