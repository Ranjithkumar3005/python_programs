from collections import Counter

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)
        print(count)
        # Sort keys by absolute value to handle negative and positive numbers properly
        for x in sorted(count, key=abs):
            print(x)
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        
        return True


s=Solution()
print(s.canReorderDoubled([2,1,2,1,1,1,2,2]))