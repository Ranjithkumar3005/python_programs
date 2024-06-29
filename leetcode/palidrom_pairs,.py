class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dum=[]
        h={}
        c="0"
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if i!=j:
                   s=words[i]+words[j]
                   if s in h:
                       s=c+s+c
                       c+="0"
                       h[s]=[i,j]
                   else:
                      h[s]=[i,j]
        for i in h:
            if i==i[::-1]:
                dum.append(h[i])
        print(dum)
        
s=Solution()
s.palindromePairs(["","adijdce","i","egjgc","jcjcj","f","hfcbdah","bhb","afie","fegc","fcbeg","fihbaga","ehgffg","gjih","ejdejg","gj","a","fbh","hg","addi"])