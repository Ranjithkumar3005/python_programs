
s =  ["xbc","pcxbcf","xb","cxbc","pcxbc"]
t = s[0]
def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length=1
        u=0
        k=0
        for i in range(1,len(s)):
            for j in range(0,len(s[i])):
                for l in range(0,len(t)):
                    if s[i][j]==t[l]:
                        print(s[i])
                        u+=1
                        length+=1
                        if len(s[i-1])==len(s[i]):
                            length-=1
                        break
                    
                  
                    
                
            print(length)      
                    
       


isSubsequence('self',s,t)




s ="abc"

t ="acab"
f=t
var=False
for i in range(0,len(s)):
     h=0
     while h<len(t):
            if t[h]==s[i]:   
               f=f.replace(t[h], '',1)
               break
            h+=1
            
            
           
    
print(f)