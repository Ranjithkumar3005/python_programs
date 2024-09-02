class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        h={}
        d=0
        for i in adjacentPairs:
            if i[0] not in h and i[1] not in h:
                h[i[0]]=[i[1]]
                d+=1
            else:
                if i[0] in h:
                    h[i[0]].append(i[1])
                    d+=1
                else:
                    h[i[1]].append(i[0])
                    d+=1
        dum=[]
        for i in h:
            dum.append(h[i][0])
            dum.append(i)
            dum.append(h[i][1])
            break
        
        while d!=len(dum):
            if dum[0] in h:
                dum.insert(0,h[dum[0]][0])
            if dum[len(dum)-1] in h:
                dum.append(h[dum[len(dum)-1]][0])
             
        print(dum)
        

s=Solution()
s.restoreArray(adjacentPairs = [[4,-2],[1,4],[-3,1]])