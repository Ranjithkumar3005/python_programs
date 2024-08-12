class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        h={}
        for i in range(0,len(words)):
            str1=""
            str2=""
            for j in range(0,len(words[i]),2):
                str1+=words[i][j]
                str1=sorted(str1)
            for k in range(1,len(words[i]),2):
                str2+=words[i][k]
                str2=sorted(str2)
            val="".join(str1)+"".join(str2)
            if val not in h:
                h[val]=1
        print(len(h))
        
        
        

s=Solution()
s.numSpecialEquivGroups( words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"])