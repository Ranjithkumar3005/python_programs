class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        h={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        h1={}
        dummy=[]
        value=0
        for i in range(0,len(words)):
            for j in range(1,len(words[i])):
               vaue=h[words[i][j]]-h[words[i][j-1]] 
               dummy.append(vaue)
            h1[words[i]]=dummy
            dummy=[]
        print(h1)
        dummy2=list(h1.items())
        i=0
        while True:
           if i==len(dummy2)-1:
               break
           if dummy2[i][1]!=dummy2[i+1][1] and dummy2[i-1][1]!=dummy2[i][1]:
               print(dummy2[i][0])
               break
           i+=1
s=Solution()
s.oddString( words = ["aaa","bbb"])