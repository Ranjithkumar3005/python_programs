class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        dum=[]
        for i in number:
            if i.isalnum():
                dum.append(i)
        strs=""
        for i in range(0,len(dum)):
            if (i+1)%3==0:
                strs+=dum[i]
                strs+="-"
            else:
                strs+=dum[i]
        strs=list(strs)
        if len(dum)%3==1:
            tem=strs[len(strs)-2]
            strs[len(strs)-2]=strs[len(strs)-3]
            strs[len(strs)-3]=tem
        print("".join(strs))
        
        
s=Solution()
s.reformatNumber("123 4-567")