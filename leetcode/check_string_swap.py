class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = 0
        if len(s1) == len(s2):
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            if count < 3:
                return sorted(s1) == sorted(s2)
        return False
        
        
s=Solution()
print(s.areAlmostEqual(s1 = "bank", s2 = "kanb"))