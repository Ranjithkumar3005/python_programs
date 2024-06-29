class Solution(object):
    def minimumTimeToInitialState(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        leng=len(word)-k+1
        min=0
        c=0
        dum=word
        h={}
        d=0
        for i in range(0,leng):
            while True:
                d+=1
                pref=dum[c:k+c]
                pref1=pref[::-1]
                suff=dum[k:len(word)]
                dum=suff+pref
                dum1=suff+pref1
                if dum in h:      
                    break
                if dum==word or dum1==word:
                    if min==0:
                        min=d
                    elif min>d:
                        min=d
                    break
                    
                h[dum]=0
                
                
            c+=1
            dum=word
            d=0
        print(min)
        
        

s=Solution()
s.minimumTimeToInitialState("abb",2)


