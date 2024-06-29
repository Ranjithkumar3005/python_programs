class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        h1={}
        h2={}
        for i in matches:
            h1[i[0]]=1
            if i[1] in h2:
                h2[i[1]]=0
            else:
                h2[i[1]]=1
        dum1=[]
        dum2=[]
        for i in h1:
            if i not in h2:
                dum1.append(i)
        for i in h2:
            if h2[i]==1:
                dum2.append(i)
        dum3=[]
        dum3.append(sorted(dum1))
        dum3.append(sorted(dum2))
        print(dum3)
        

s=Solution()
s.findWinners(matches = [[2,3],[1,3],[5,4],[6,4]])