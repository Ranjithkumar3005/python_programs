class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        h={}
        
        for i in words:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        so = sorted(h.items(), key=lambda x: x[1], reverse=True)
        dum=[]
        dum1=[]
        print(so)
        dum1.append(so[0][0])
        for i in range(1,k):
            if so[i][1]!=so[i-1][1]:
                if dum1!=[]:
                    dum1=sorted(dum1)
                    dum+=dum1
                    dum1=[]
                dum.append(so[i][0])
            else:
                dum1.append(so[i][0])

        if dum1!=[]:
            dum+=sorted(dum1)
        print(dum)
        
s=Solution()
s.topKFrequent(["aaa","aa","a"])