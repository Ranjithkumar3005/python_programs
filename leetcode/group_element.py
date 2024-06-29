class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        h={}
        h1={}
        for i in groupSizes:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        for i in range(0,len(groupSizes)):
            h[i]=groupSizes[i]
        dum=[]
        c=1
        d=0
        du=[]
        while True:
            print(c)
            for i in h:
              if h[i]==c and h[i]!=-1:
                h1[c]-=1
                d+=1
                h[i]=-1
                du.append(i)
                if len(du)==c:
                    break
            if du!=[]:
              dum.append(du)
              du=[]
            if c not in h1 or h1[c]==0:
              c+=1
            if d==len(h):
                break
        print(dum)
s=Solution()
s.groupThePeople(groupSizes = [3,3,3,3,3,1,3])