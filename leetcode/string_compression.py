class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==1:
            return len(chars)
        c=1
        
        dum=[]
        tem=""
        for i in range(0,len(chars)-1):
            tem=chars[i]
            if chars[i]==chars[i+1]:
                c+=1
            else:
                if c==1:
                  dum.append(tem)
                else:
                    dum.append(tem)
                    c=str(c)
                    for i in range(0,len(c)):
                        dum.append(c[i])
                c=1
                tem=""
        if c==1:
            dum.append(chars[len(chars)-1])
        else:
            dum.append(chars[len(chars)-1])
            c=str(c)
            for i in range(0,len(c)):
                dum.append(c[i])
        for i in range(0,len(dum)):
            chars[i]=dum[i]
        print(dum)
        return len(dum)
    

  
        

s=Solution()
print(s.compress( ["a","a","a","a","a","b"]))