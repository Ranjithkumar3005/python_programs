class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        """
        i = cur = 0
        for j in range(1, len(skills)):
            if skills[i] < skills[j]:
                cur = 0
                i = j
            cur += 1
            if cur == k:
                break
        return i               
        
s=Solution()
print(s.findWinningPlayer( skills = [4,2,6,3,9], k = 2))