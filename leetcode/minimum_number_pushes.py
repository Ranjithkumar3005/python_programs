class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        if len(word)<=8:
            return len(word)
        h={}
        for i in word:
            if i in h:
                h[i]+=1
            else:
               h[i]=1
        
        so = sorted(h.items(), key=lambda x: x[1], reverse=True)
        c=8
        sum=0
        i=0
        while i<len(so):
            sum+=((c//8)*so[i][1])
            i+=1
            c+=1
        print(sum)
        

s=Solution()
s.minimumPushes( word = "abcde")