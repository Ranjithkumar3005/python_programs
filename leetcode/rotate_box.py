class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        
        k=0
        dum1=[[0 for _ in range(len(box))] for _ in range(len(box[0]))]

        for i in range(len(box)-1,-1,-1):
            c=len(box[i])-1
            dum=["."]*(c+1)
            for j in range(len(box[i])-1,-1,-1):
                if box[i][j]=="#":
                    dum[c]="#"
                    c-=1
                elif box[i][j]==".":
                    continue
                elif box[i][j]=="*":
                    dum[j]="*"
                    c=j-1
            for i in range(0,len(dum)):
                dum1[i][k]=dum[i]
            k+=1
        print(dum1)

s=Solution()
s.rotateTheBox( box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]])