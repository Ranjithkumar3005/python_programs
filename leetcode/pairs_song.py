class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        h = {}
        c = 0
        
        for t in time:
            # Find the complementary remainder
            complement = (60 - t % 60) % 60
            
            # If the complement exists in the dictionary, add its count to c
            if complement in h:
                c += h[complement]
            
            # Add the current remainder to the dictionary
            remainder = t % 60
            if remainder in h:
                h[remainder] += 1
            else:
                h[remainder] = 1
        
        return c

s = Solution()
print(s.numPairsDivisibleBy60([30, 20, 150, 100, 40]))  # Output should be 3
