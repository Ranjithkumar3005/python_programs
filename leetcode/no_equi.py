class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        c=0
        d=dominoes
        h={}
        for domi in dominoes:
            p = tuple(sorted(domi))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        c = 0
        for n in d.values():
            s = n*(n-1)//2
            c += s
        return c
        
        

s=Solution()
s.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]])