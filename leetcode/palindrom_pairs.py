class Solution:
    def palindromePairs(self, words):
        dum=[]
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                   if i==j:
                       continue
                   s=words[i]+words[j]
                   rev=s[::-1]
                   if s==rev:
                       dum.append([i,j])
        return dum
    
    
    
s=Solution()
print(s.palindromePairs(words = ["abcd","dcba","lls","s","sssll"]))