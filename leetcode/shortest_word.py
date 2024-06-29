class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate=licensePlate.lower()
        h={}
        d=[]
        dummy=[]
        for i in range(0,len(licensePlate)):
           if licensePlate[i].isalpha() and licensePlate[i] not in h:
              h[licensePlate[i]]=licensePlate.count(licensePlate[i])
        count=0
        for i in range(0,len(words)):
            count=0
            d=[]
            for j in range(0,len(words[i])):
                if words[i][j] in h and words[i][j] not in d:
                    if h[words[i][j]]<=words[i].count(words[i][j]):
                        count+=1
                        d.append(words[i][j])
                    else:
                        break
            if count==len(h):
                dummy.append(words[i])
        print(h)
        if dummy !=[]:
            min=len(dummy[0])
            for i in dummy:
              if len(i)<min:
                min=len(i)
        
            for i in dummy:
              if len(i)==min:
                return i
        return "Null"
        
s=Solution()
print(s.shortestCompletingWord(licensePlate ="GrC8950",words =["measure","other","every","base","according","level","meeting","none","marriage","rest"]))