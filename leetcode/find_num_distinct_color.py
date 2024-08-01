class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        h={}
        d=[]
        h1={}
        for i in range(0,len(queries)):
            h1[queries[i][1]]=0
            if queries[i][1] not in h1:
             h[queries[i][0]]=queries[i][1]
            d.append(len(h))
        print(d)
        

s=Solution()
s.queryResults(limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]])