import math
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        dum=[]
        
        potions=sorted(potions)
        n=len(potions)
        pairs=[0]*len(spells)
        for i in range(0,len(spells)):
            spell=spells[i]
            left = 0
            right = n-1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = n - left
        print(pairs)

s=Solution()
s.successfulPairs( spells = [5,1,3], potions = [1,2,3,4,5], success = 7)