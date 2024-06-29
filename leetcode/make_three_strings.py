class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        s = len(s1) + len(s2) + len(s3)
        n = min(len(s1), len(s2), len(s3))
        for i in range(n):
            if not s1[i] == s2[i] == s3[i]:
                return -1 if i == 0 else s - 3 * i
        return s - 3 * n

        
s=Solution()
print(s.findMinimumOperations(s1 = "ab", s2 = "abc", s3 = "abd"))