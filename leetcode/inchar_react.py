from collections import defaultdict
from math import gcd

class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        ratio_count = defaultdict(int)
        
        for w, h in rectangles:
            g = gcd(w, h)
            simplified_ratio = (w // g, h // g)
            ratio_count[simplified_ratio] += 1
        
        #print(ratio_count)
        
        result = 0
        for count in ratio_count.values():
            if count > 1:
                result += (count * (count - 1)) // 2  # nC2 = n(n-1)/2
        
        return result

s = Solution()
print(s.interchangeableRectangles(rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]]))
