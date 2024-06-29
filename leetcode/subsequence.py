s = "ab"
t = "baab"

def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        u=0
        k=0
        for i in range(0,len(s)):
            for j in range(k,len(t)):
                if s[i]==t[j]:
                    print(s[i])
                    u+=1
                    k=j+1
                    break
                
                    
                    
        if u==len(s):
            return "True"
        else:
            return "False"


d=isSubsequence('self',s,t)
print(d)

             