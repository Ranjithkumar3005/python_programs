class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        h={}
        for i in range(0,len(creators)):
            if creators[i] in h:
                h[creators[i]][0]+=views[i]
                if ids[i] in h[creators[i]][1]:
                    h[creators[i]][1][ids[i]]+=views[i]
                else:
                    h[creators[i]][1][ids[i]]=views[i]
            else:
                h[creators[i]]=[views[i],{}]
                h[creators[i]][1][ids[i]]=views[i]
        vals=list(h.values())
        max1=0
        for i in vals:
            max1=max(max1,i[0])
        dum=[]
        
        for i in h:
            d=[]
            if h[i][0]==max1:
                val1=max(h[i][1].values())
                for j in h[i][1]:
                    if h[i][1][j]==val1:
                        d.append(j)
                dum.append([i,sorted(d)[0]])
        print(dum)
                    
        
        

s=Solution()
s.mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4])