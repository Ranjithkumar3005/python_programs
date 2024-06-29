class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        for l in mat:
            n = len(l)
            for i in range(n):
                if l[i] != l[(i + k) % n]:
                    return False
        return True
        
s=Solution()
print(s.areSimilar(mat = [[1,2]], k = 1))