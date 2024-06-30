class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        h1={}
        h2={}
        for i in range(1,n+1):
            h1[i]=0
            h2[i]=0
        for i in range(0,len(edges)):
            if edges[i][0]==3:
                h1[edges[i][1]]+=1
                h2[edges[i][1]]+=1
            elif edges[i][0]==2:
                h2[edges[i][1]]+=1
            else:
                h1[edges[i][1]]+=1
        print(h1," ",h2)
        

s=Solution()
s.maxNumEdgesToRemove( n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])