class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        c=text.count(" ")
        dummy=text.split(" ")
        count=0
        for i in dummy:
            if i.isalpha():
                count+=1
        strs=""
        if c==0:
            return text
        elif count==1:
            for i in dummy:
             if i!="":
              strs+=i
            for i in range(0,c):
                strs+=" "
            return strs
        r=c//(count-1)
        strs=""
        m=0
        for i in dummy:
            if i!="":
              m+=1
              strs+=i
              if m==count:
                  break
              for j in range(0,r):
                strs+=" "
        d=c-(r*(count-1))
        print(d)
        if d!=0:
            for i in range(0,d):
                strs+=" "
            
        print(strs)
        
s=Solution()
print(s.reorderSpaces(text = " a "))