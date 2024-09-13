class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        h={}
        for i in items1:
            if i[0] in h:
                h[i[0]]+=i[1]
            else:
                h[i[0]]=i[1]
        
        for i in items2:
            if i[0] in h:
                h[i[0]]+=i[1]
            else:
                h[i[0]]=i[1]
        
        dum=[]
        for i in h:
            dum.append([i,h[i]])
        return sorted(dum)
        

s=Solution()
print(s.mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))