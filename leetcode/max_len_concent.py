class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
       
        dum=[]
        for i in arr:
            d=set(i)
            if len(i)==len(d):
                dum.append(i)
        max=0
        for i in range(len(dum)-1,-1,-1):
            dum1=dum[i]
            for j in range(len(dum)-1,-1,-1):
                se=dum1
                dum1+=dum[j]
                if len(dum1)==len(set(dum1)):
                    if max<len(dum1):
                        max=len(dum1)
                else:
                    dum1=se
            if max<len(dum[i]):
                        max=len(dum[i])
               
        print(max)   
        
        

s=Solution()
print(s.maxLength(["abc","ax","dlmn","dy"]))