class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        h={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        dummy=[]
        check=True
        for i in range(0,len(s)-1):
            if s[i] not in dummy:
                dummy.append(s[i])
                if (i+distance[h[s[i]]]+1)>=len(s):
                    check=False
                elif s[i]!=s[i+distance[h[s[i]]]+1]:
                    print(s[i]," ",s[i+distance[h[s[i]]]])
                    check=False
        return check

s=Solution()
print(s.checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))